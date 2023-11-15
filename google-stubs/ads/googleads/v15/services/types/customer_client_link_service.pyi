from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v15.resources.types.customer_client_link import (
    CustomerClientLink,
)

_M = TypeVar("_M")

class CustomerClientLinkOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerClientLink
    update: CustomerClientLink
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CustomerClientLink = ...,
        update: CustomerClientLink = ...
    ) -> None: ...

class MutateCustomerClientLinkRequest(proto.Message):
    customer_id: str
    operation: CustomerClientLinkOperation
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: CustomerClientLinkOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerClientLinkResponse(proto.Message):
    result: MutateCustomerClientLinkResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateCustomerClientLinkResult = ...
    ) -> None: ...

class MutateCustomerClientLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
