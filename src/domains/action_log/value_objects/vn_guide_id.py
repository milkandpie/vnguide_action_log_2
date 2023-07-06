from clean_architecture.domains import ValueObject


class VNGuideId(ValueObject):
    def __init__(self, _id: str):
        self.__id = _id

    def get_comparable(self):
        return self.__id
