from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.customer_customizer import (
    CustomerCustomizer,
)

class CustomerCustomizerOperation(proto.Message):
    create: CustomerCustomizer
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CustomerCustomizer = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerCustomizerResult(proto.Message):
    resource_name: str
    customer_customizer: CustomerCustomizer
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer_customizer: CustomerCustomizer = ...
    ) -> None: ...

class MutateCustomerCustomizersRequest(proto.Message):
    customer_id: str
    operations: list[CustomerCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerCustomizerOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomerCustomizersResponse(proto.Message):
    results: list[MutateCustomerCustomizerResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomerCustomizerResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
