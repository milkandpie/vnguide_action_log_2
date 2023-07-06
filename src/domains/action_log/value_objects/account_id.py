from clean_architecture.domains import EntityId


class AccountId(EntityId):
    @staticmethod
    def create() -> 'AccountId':
        return AccountId(super().create().get_comparable())
