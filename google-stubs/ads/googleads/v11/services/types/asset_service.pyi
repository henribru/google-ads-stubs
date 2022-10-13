from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.asset import Asset

class AssetOperation(proto.Message):
    update_mask: FieldMask
    create: Asset
    update: Asset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: Asset = ...,
        update: Asset = ...
    ) -> None: ...

class MutateAssetResult(proto.Message):
    resource_name: str
    asset: Asset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset: Asset = ...
    ) -> None: ...

class MutateAssetsRequest(proto.Message):
    customer_id: str
    operations: list[AssetOperation]
    partial_failure: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AssetOperation] = ...,
        partial_failure: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAssetsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAssetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAssetResult] = ...
    ) -> None: ...
