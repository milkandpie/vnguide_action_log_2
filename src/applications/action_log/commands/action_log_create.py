from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from clean_architecture import Command, Repository, CommandHandleable
from src.domains import (ActionLog, ActionLogCreatableIn)


@dataclass
class ActionLogCreatingCommand(Command):
    email: str
    vn_guide_type: str
    vn_guide_id: str
    action: str
    log: str
    generated_at: datetime
    account_id: str = None
    object_id: str = None
    action_log_id: str = None

    # TODO: Validate command


class ActionLogCreatingRepository(Repository, ABC):
    @abstractmethod
    async def create(self, command: ActionLogCreatingCommand) -> ActionLog:
        pass

    @abstractmethod
    async def save(self, action_log: ActionLog) -> ActionLog:
        pass


class ActionLogCreatingService(CommandHandleable):
    def __init__(self, repository: ActionLogCreatingRepository):
        super().__init__()
        self.__repository = repository

    async def handle(self, command: ActionLogCreatingCommand):
        action_log = await self.__repository.create(command)
        action_log.create(ActionLogCreatableIn(command.email, command.vn_guide_type, command.vn_guide_id,
                                               command.action, command.log, command.generated_at,
                                               account_id=command.account_id,
                                               object_id=command.object_id,
                                               action_log_id=command.action_log_id))
        await self.__repository.save(action_log)
