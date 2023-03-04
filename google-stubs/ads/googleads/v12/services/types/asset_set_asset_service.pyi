from collections.abc import MutableSequence
from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v12.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v12.resources.types.asset_set_asset import AssetSetAsset

class AssetSetAssetOperation(proto.Message):
    create: AssetSetAsset
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AssetSetAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetSetAssetResult(proto.Message):
    resource_name: str
    asset_set_asset: AssetSetAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_set_asset: AssetSetAsset = ...
    ) -> None: ...

class MutateAssetSetAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetSetAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[AssetSetAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAssetSetAssetsResponse(proto.Message):
    results: MutableSequence[MutateAssetSetAssetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[MutateAssetSetAssetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
