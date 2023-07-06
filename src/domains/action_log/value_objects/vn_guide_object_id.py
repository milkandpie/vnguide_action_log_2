from clean_architecture.domains import EntityId


class VNGuideObjectId(EntityId):

    @staticmethod
    def create() -> 'VNGuideObjectId':
        return VNGuideObjectId(super().create().get_comparable())
