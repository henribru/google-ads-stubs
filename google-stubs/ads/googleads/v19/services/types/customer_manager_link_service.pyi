from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v19.resources.types.customer_manager_link import CustomerManagerLink
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerManagerLinkOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerManagerLink
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., update: CustomerManagerLink = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "update"]) -> bool: ...
class MoveManagerLinkRequest(proto.Message):
    customer_id: str
    previous_customer_manager_link: str
    new_manager: str
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., previous_customer_manager_link: str = ..., new_manager: str = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "previous_customer_manager_link", "new_manager", "validate_only"]) -> bool: ...
class MoveManagerLinkResponse(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateCustomerManagerLinkRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerManagerLinkOperation]
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[CustomerManagerLinkOperation] = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "validate_only"]) -> bool: ...
class MutateCustomerManagerLinkResponse(proto.Message):
    results: MutableSequence[MutateCustomerManagerLinkResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., results: MutableSequence[MutateCustomerManagerLinkResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results"]) -> bool: ...
class MutateCustomerManagerLinkResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
