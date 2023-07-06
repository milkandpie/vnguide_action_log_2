from clean_architecture.domains import ValueObject


class VNGuideType(ValueObject):
    def __init__(self, _type: str):
        self.__type = _type

    def get_comparable(self):
        return self.__type
