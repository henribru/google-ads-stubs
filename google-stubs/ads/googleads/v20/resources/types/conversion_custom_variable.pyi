from google.ads.googleads.v20.enums.types.conversion_custom_variable_status import ConversionCustomVariableStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionCustomVariable(proto.Message):
    resource_name: str
    id: int
    name: str
    tag: str
    status: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    owner_customer: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., name: str = ..., tag: str = ..., status: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus = ..., owner_customer: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "name", "tag", "status", "owner_customer"]) -> bool: ...
