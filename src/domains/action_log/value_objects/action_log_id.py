from clean_architecture.domains import EntityId


class ActionLogId(EntityId):
    @staticmethod
    def create() -> 'ActionLogId':
        return ActionLogId(super().create().get_comparable())
