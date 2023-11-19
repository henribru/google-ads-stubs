from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v14.resources.types.customer_user_access import (
    CustomerUserAccess,
)

_M = TypeVar("_M")

class CustomerUserAccessOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerUserAccess
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        update: CustomerUserAccess = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "update", "remove"]) -> bool: ...  # type: ignore[override]

class MutateCustomerUserAccessRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: CustomerUserAccessOperation = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operation"]) -> bool: ...  # type: ignore[override]

class MutateCustomerUserAccessResponse(proto.Message):
    result: MutateCustomerUserAccessResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateCustomerUserAccessResult = ...
    ) -> None: ...
    def __contains__(self, key: Literal["result"]) -> bool: ...  # type: ignore[override]

class MutateCustomerUserAccessResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]
