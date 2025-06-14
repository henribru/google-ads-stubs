from google.ads.googleads.v18.enums.types.manager_link_status import ManagerLinkStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerManagerLink(proto.Message):
    resource_name: str
    manager_customer: str
    manager_link_id: int
    status: ManagerLinkStatusEnum.ManagerLinkStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., manager_customer: str = ..., manager_link_id: int = ..., status: ManagerLinkStatusEnum.ManagerLinkStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "manager_customer", "manager_link_id", "status"]) -> bool: ...
