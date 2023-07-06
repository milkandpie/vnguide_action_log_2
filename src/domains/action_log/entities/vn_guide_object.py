from dataclasses import dataclass

from clean_architecture.domains import Entity, EntityId
from ..value_objects import VNGuideType, VNGuideId, VNGuideObjectId


class VNGuideObject(Entity):
    def __init__(self, _id: EntityId, vn_guide_id: VNGuideId, vn_guide_type: VNGuiredeType):
        super().__init__(_id)
        self.__vn_guide_id = vn_guide_id
        self.__vn_guide_type = vn_guide_type

    @property
    def vn_guide_id(self):
        return self.__vn_guide_id

    @property
    def vn_guide_type(self):
        return self.__vn_guide_type

    def __eq__(self, other: 'VNGuideObject'):
        return other.vn_guide_type == self.vn_guide_type and other.vn_guide_id == self.vn_guide_id

    def __repr__(self):
        return f'{self.vn_guide_type}:{self.vn_guide_id}'

    @staticmethod
    def create(vn_guide_id: str, vn_guide_type: str,
               _id: str = None):
        object_id = VNGuideObjectId(_id) if _id else VNGuideObjectId.create()
        return VNGuideObject(object_id, VNGuideId(vn_guide_id), VNGuideType(vn_guide_type))

    def to_dict(self) -> dict:
        return {
            **super().to_dict(),
            'vn_guide_id': self.__vn_guide_id,
            'vn_guide_type': self.__vn_guide_type
        }
