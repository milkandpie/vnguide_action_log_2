from uuid import UUID

from beanie.odm.operators.update.general import Set
from clean_architecture import BasedRepositoryInjector
from clean_architecture.infrastructure.persistences.mongo.common import MongoClientFactory
from clean_architecture.infrastructure.persistences.mongo.config import GENERAL_MONGO_CONFIG
from pymongo.client_session import ClientSession

from src.applications import ActionLogCreatingRepository, ActionLogCreatingCommand
from src.domains import (
    ActionLog, Account, VNGuideObject,
    AccountId, ActionLogId, VNGuideObjectId,
    VNGuideType)
from src.infrastructure.persistents.models import AccountDAO, ActionLogDAO, VNGuideObjectDAO


class MongoActionLogCreatingRepository(ActionLogCreatingRepository):
    def __init__(self,
                 session: ClientSession = None,
                 injector: BasedRepositoryInjector = None):
        self.__session = session
        self.__injector = injector

    async def create(self, command: ActionLogCreatingCommand) -> ActionLog:
        if command.action_log_id:
            action_log_document = await (ActionLogDAO.
                                         find({'id': UUID(command.action_log_id)},
                                              session=self.__session).
                                         first_or_none())
            if action_log_document:
                raise Exception()

        account_document = await (AccountDAO.
                                  find({'email': command.email},
                                       session=self.__session).
                                  first_or_none())

        if account_document:
            account = Account(AccountId(account_document.id),
                              email=command.email)
        else:
            account = Account.create(command.email)

        object_document = await (VNGuideObjectDAO.
                                 find({'vn_guide_id': command.vn_guide_id,
                                       'vn_guide_type': command.vn_guide_type},
                                      session=self.__session).
                                 first_or_none())

        if object_document:
            _object = VNGuideObject(VNGuideObjectId(object_document.id),
                                    vn_guide_id=object_document.vn_guide_id,
                                    vn_guide_type=VNGuideType(object_document.vn_guide_type))
        else:
            _object = VNGuideObject.create(vn_guide_id=command.vn_guide_id,
                                           vn_guide_type=command.vn_guide_type)

        if command.action_log_id:
            action_log_id = ActionLogId(command.action_log_id)
        else:
            action_log_id = ActionLogId.create()

        return ActionLog(action_log_id, account, _object, command.action, command.log, command.generated_at)

    async def save(self, action_log: ActionLog) -> ActionLog:
        if self.__session:
            return await self._save(action_log, self.__session)

        factory = MongoClientFactory()
        client = factory.create(GENERAL_MONGO_CONFIG)
        async with await client.start_session() as session:
            async with session.start_transaction():
                return await self._save(action_log, self.__session)

    async def _save(self, action_log: ActionLog, session: ClientSession) -> ActionLog:
        await(ActionLogDAO.
              find_one(ActionLogDAO.id == UUID(str(action_log))).
              upsert(Set(action_log.to_dict()),
                     on_insert=ActionLogDAO(**action_log.to_dict()),
                     session=session))

        account = action_log.account
        await(AccountDAO.
              find_one(AccountDAO.id == UUID(str(account))).
              upsert(Set(account.to_dict()),
                     on_insert=AccountDAO(**account.to_dict()),
                     session=session))

        _object = action_log.vn_guide_object
        await(VNGuideObjectDAO.
              find_one(VNGuideObjectDAO.id == UUID(str(_object))).
              upsert(Set(_object.to_dict()),
                     on_insert=VNGuideObjectDAO(**_object.to_dict()),
                     session=session))

        self.__injector.set_concreate({ClientSession: session})
        return action_log
