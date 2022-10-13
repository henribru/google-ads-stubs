from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.customer_asset import CustomerAsset

class CustomerAssetOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerAsset
    update: CustomerAsset
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomerAsset = ...,
        update: CustomerAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerAssetResult(proto.Message):
    resource_name: str
    customer_asset: CustomerAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer_asset: CustomerAsset = ...
    ) -> None: ...

class MutateCustomerAssetsRequest(proto.Message):
    customer_id: str
    operations: list[CustomerAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomerAssetsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCustomerAssetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCustomerAssetResult] = ...
    ) -> None: ...
