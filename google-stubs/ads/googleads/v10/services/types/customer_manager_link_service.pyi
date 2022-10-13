from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v10.resources.types.customer_manager_link import (
    CustomerManagerLink,
)

class CustomerManagerLinkOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerManagerLink
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: CustomerManagerLink = ...
    ) -> None: ...

class MoveManagerLinkRequest(proto.Message):
    customer_id: str
    previous_customer_manager_link: str
    new_manager: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        previous_customer_manager_link: str = ...,
        new_manager: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class MoveManagerLinkResponse(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomerManagerLinkRequest(proto.Message):
    customer_id: str
    operations: list[CustomerManagerLinkOperation]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerManagerLinkOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerManagerLinkResponse(proto.Message):
    results: list[MutateCustomerManagerLinkResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomerManagerLinkResult] = ...
    ) -> None: ...

class MutateCustomerManagerLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
