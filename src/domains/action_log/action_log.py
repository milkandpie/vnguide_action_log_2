from dataclasses import dataclass
from datetime import datetime

from clean_architecture.domains import AggregateRoot

from .entities import Account, VNGuideObject
from .value_objects import ActionLogId


@dataclass
class ActionLogCreatableIn:
    email: str
    vn_guide_type: str
    vn_guide_id: str
    action: str
    log: str
    generated_at: datetime
    account_id: str = None
    object_id: str = None
    action_log_id: str = None


class ActionLog(AggregateRoot):
    def __init__(self, _id: ActionLogId, account: Account, vn_guide_object: VNGuideObject,
                 action: str, log: str, generated_at: datetime):
        super().__init__(_id)
        self.__account = account
        self.__vn_guide_object = vn_guide_object
        self.__generated_at = generated_at
        self.__action = action
        self.__log = log

    @property
    def vn_guide_object(self):
        return self.__vn_guide_object

    @property
    def account(self):
        return self.__account

    def create(self, dto: ActionLogCreatableIn) -> 'ActionLog':
        if self.get_comparable() == dto.action_log_id:
            raise Exception

        return self._create(dto)

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            'log': self.__log,
            'action': self.__action,
            'generated_at': self.__generated_at,
            'account_id': self.__account.get_id(),
            'object_id': self.__vn_guide_object.get_id()
        }

    @staticmethod
    def _create(dto: ActionLogCreatableIn) -> 'ActionLog':
        return ActionLog(ActionLogId.create(),
                         Account.create(dto.email, account_id=dto.account_id),
                         VNGuideObject.create(dto.vn_guide_type, dto.vn_guide_id, _id=dto.object_id),
                         dto.action, dto.log, dto.generated_at)
