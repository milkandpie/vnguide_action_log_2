from clean_architecture import BasedRepositoryInjector
from pymongo.client_session import ClientSession

from src.applications import ActionLogCreatingRepository
from .repositories import MongoActionLogCreatingRepository


class BasedMongoInjector(BasedRepositoryInjector):
    def __init__(self):
        super().__init__({
            ClientSession: None,
            ActionLogCreatingRepository: MongoActionLogCreatingRepository
        })
