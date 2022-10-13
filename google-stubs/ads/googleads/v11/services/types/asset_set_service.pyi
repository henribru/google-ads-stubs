from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.asset_set import AssetSet

class AssetSetOperation(proto.Message):
    update_mask: FieldMask
    create: AssetSet
    update: AssetSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AssetSet = ...,
        update: AssetSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetSetResult(proto.Message):
    resource_name: str
    asset_set: AssetSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_set: AssetSet = ...
    ) -> None: ...

class MutateAssetSetsRequest(proto.Message):
    customer_id: str
    operations: list[AssetSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AssetSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAssetSetsResponse(proto.Message):
    results: list[MutateAssetSetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAssetSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
