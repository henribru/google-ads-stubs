from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.resources.types.customer_sk_ad_network_conversion_value_schema import (
    CustomerSkAdNetworkConversionValueSchema,
)

_M = TypeVar("_M")

class CustomerSkAdNetworkConversionValueSchemaOperation(proto.Message):
    update: CustomerSkAdNetworkConversionValueSchema
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update: CustomerSkAdNetworkConversionValueSchema = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update"]) -> bool: ...  # type: ignore[override]

class MutateCustomerSkAdNetworkConversionValueSchemaRequest(proto.Message):
    customer_id: str
    operation: CustomerSkAdNetworkConversionValueSchemaOperation
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: CustomerSkAdNetworkConversionValueSchemaOperation = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operation", "validate_only"]) -> bool: ...  # type: ignore[override]

class MutateCustomerSkAdNetworkConversionValueSchemaResponse(proto.Message):
    result: MutateCustomerSkAdNetworkConversionValueSchemaResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateCustomerSkAdNetworkConversionValueSchemaResult = ...
    ) -> None: ...
    def __contains__(self, key: Literal["result"]) -> bool: ...  # type: ignore[override]

class MutateCustomerSkAdNetworkConversionValueSchemaResult(proto.Message):
    resource_name: str
    app_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        app_id: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "app_id"]) -> bool: ...  # type: ignore[override]
