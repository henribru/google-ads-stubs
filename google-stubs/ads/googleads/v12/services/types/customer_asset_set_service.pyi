from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v12.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v12.resources.types.customer_asset_set import CustomerAssetSet

class CustomerAssetSetOperation(proto.Message):
    create: CustomerAssetSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CustomerAssetSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerAssetSetResult(proto.Message):
    resource_name: str
    customer_asset_set: CustomerAssetSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer_asset_set: CustomerAssetSet = ...
    ) -> None: ...

class MutateCustomerAssetSetsRequest(proto.Message):
    customer_id: str
    operations: list[CustomerAssetSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerAssetSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomerAssetSetsResponse(proto.Message):
    results: list[MutateCustomerAssetSetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomerAssetSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
