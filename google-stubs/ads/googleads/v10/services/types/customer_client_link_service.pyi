from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v10.resources.types.customer_client_link import (
    CustomerClientLink,
)

class CustomerClientLinkOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerClientLink
    update: CustomerClientLink
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomerClientLink = ...,
        update: CustomerClientLink = ...
    ) -> None: ...

class MutateCustomerClientLinkRequest(proto.Message):
    customer_id: str
    operation: CustomerClientLinkOperation
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: CustomerClientLinkOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerClientLinkResponse(proto.Message):
    result: MutateCustomerClientLinkResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateCustomerClientLinkResult = ...
    ) -> None: ...

class MutateCustomerClientLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
