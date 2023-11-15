from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v15.resources.types.customer_user_access import (
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

class MutateCustomerUserAccessResponse(proto.Message):
    result: MutateCustomerUserAccessResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateCustomerUserAccessResult = ...
    ) -> None: ...

class MutateCustomerUserAccessResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
