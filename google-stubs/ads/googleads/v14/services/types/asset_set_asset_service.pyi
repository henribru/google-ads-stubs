from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.asset_set_asset import AssetSetAsset

_M = TypeVar("_M")

class AssetSetAssetOperation(proto.Message):
    create: AssetSetAsset
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AssetSetAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetSetAssetResult(proto.Message):
    resource_name: str
    asset_set_asset: AssetSetAsset
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[MutateAssetSetAssetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
