from google.ads.googleads.v20.resources.types.customer_user_access import CustomerUserAccess
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerUserAccessOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerUserAccess
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., update: CustomerUserAccess = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "update", "remove"]) -> bool: ...
class MutateCustomerUserAccessRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessOperation
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operation: CustomerUserAccessOperation = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operation"]) -> bool: ...
class MutateCustomerUserAccessResponse(proto.Message):
    result: MutateCustomerUserAccessResult
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., result: MutateCustomerUserAccessResult = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["result"]) -> bool: ...
class MutateCustomerUserAccessResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
