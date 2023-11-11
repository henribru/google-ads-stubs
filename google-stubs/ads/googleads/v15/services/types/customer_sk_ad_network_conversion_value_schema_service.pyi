from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.resources.types.customer_sk_ad_network_conversion_value_schema import (
    CustomerSkAdNetworkConversionValueSchema,
)

_M = TypeVar("_M")

class CustomerSkAdNetworkConversionValueSchemaOperation(proto.Message):
    update: CustomerSkAdNetworkConversionValueSchema
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update: CustomerSkAdNetworkConversionValueSchema = ...
    ) -> None: ...

class MutateCustomerSkAdNetworkConversionValueSchemaRequest(proto.Message):
    customer_id: str
    operation: CustomerSkAdNetworkConversionValueSchemaOperation
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: CustomerSkAdNetworkConversionValueSchemaOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerSkAdNetworkConversionValueSchemaResponse(proto.Message):
    result: MutateCustomerSkAdNetworkConversionValueSchemaResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateCustomerSkAdNetworkConversionValueSchemaResult = ...
    ) -> None: ...

class MutateCustomerSkAdNetworkConversionValueSchemaResult(proto.Message):
    resource_name: str
    app_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        app_id: str = ...
    ) -> None: ...
