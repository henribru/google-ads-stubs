from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v13.resources.types.customer_manager_link import (
    CustomerManagerLink,
)

_M = TypeVar("_M")

class CustomerManagerLinkOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerManagerLink
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        update: CustomerManagerLink = ...
    ) -> None: ...

class MoveManagerLinkRequest(proto.Message):
    customer_id: str
    previous_customer_manager_link: str
    new_manager: str
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        previous_customer_manager_link: str = ...,
        new_manager: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class MoveManagerLinkResponse(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomerManagerLinkRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerManagerLinkOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CustomerManagerLinkOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerManagerLinkResponse(proto.Message):
    results: MutableSequence[MutateCustomerManagerLinkResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCustomerManagerLinkResult] = ...
    ) -> None: ...

class MutateCustomerManagerLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
