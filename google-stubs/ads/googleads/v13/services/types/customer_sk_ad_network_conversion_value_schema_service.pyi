from typing import Any

import proto

from google.ads.googleads.v13.resources.types.customer_sk_ad_network_conversion_value_schema import (
    CustomerSkAdNetworkConversionValueSchema,
)

class CustomerSkAdNetworkConversionValueSchemaOperation(proto.Message):
    update: CustomerSkAdNetworkConversionValueSchema
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update: CustomerSkAdNetworkConversionValueSchema = ...
    ) -> None: ...

class MutateCustomerSkAdNetworkConversionValueSchemaRequest(proto.Message):
    customer_id: str
    operation: CustomerSkAdNetworkConversionValueSchemaOperation
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: CustomerSkAdNetworkConversionValueSchemaOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerSkAdNetworkConversionValueSchemaResponse(proto.Message):
    result: MutateCustomerSkAdNetworkConversionValueSchemaResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateCustomerSkAdNetworkConversionValueSchemaResult = ...
    ) -> None: ...

class MutateCustomerSkAdNetworkConversionValueSchemaResult(proto.Message):
    resource_name: str
    app_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        app_id: str = ...
    ) -> None: ...
