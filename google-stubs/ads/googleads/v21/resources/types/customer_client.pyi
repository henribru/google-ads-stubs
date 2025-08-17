from google.ads.googleads.v21.enums.types.customer_status import CustomerStatusEnum
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerClient(proto.Message):
    resource_name: str
    client_customer: str
    hidden: bool
    level: int
    time_zone: str
    test_account: bool
    manager: bool
    descriptive_name: str
    currency_code: str
    id: int
    applied_labels: MutableSequence[str]
    status: CustomerStatusEnum.CustomerStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., client_customer: str = ..., hidden: bool = ..., level: int = ..., time_zone: str = ..., test_account: bool = ..., manager: bool = ..., descriptive_name: str = ..., currency_code: str = ..., id: int = ..., applied_labels: MutableSequence[str] = ..., status: CustomerStatusEnum.CustomerStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "client_customer", "hidden", "level", "time_zone", "test_account", "manager", "descriptive_name", "currency_code", "id", "applied_labels", "status"]) -> bool: ...
