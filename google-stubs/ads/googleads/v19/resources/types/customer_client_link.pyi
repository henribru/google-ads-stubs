import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import manager_link_status

__protobuf__: Incomplete

class CustomerClientLink(proto.Message):
    resource_name: str
    client_customer: str
    manager_link_id: int
    status: manager_link_status.ManagerLinkStatusEnum.ManagerLinkStatus
    hidden: bool
