from clean_architecture.domains import Entity
from ..value_objects import AccountId


class Account(Entity):
    def __init__(self, _id: AccountId, email: str):
        super().__init__(_id)
        self.__email = email

    @staticmethod
    def create(email, account_id: str = None) -> 'Account':
        account_id = AccountId(account_id) if account_id else AccountId.create()
        return Account(account_id, email)

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            'email': self.__email
        }
