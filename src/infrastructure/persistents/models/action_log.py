from beanie import Indexed
from clean_architecture.infrastructure.persistences.mongo.models._based_document import BasedDocument


class ActionLogDAO(BasedDocument):
    account_id: Indexed(str)
    object_id: Indexed(str)
    generated_at: str
    action: str
    log: str


class AccountDAO(BasedDocument):
    email: Indexed(str)


class VNGuideObjectDAO(BasedDocument):
    vn_guide_id: Indexed(str)
    vn_guide_type: str
