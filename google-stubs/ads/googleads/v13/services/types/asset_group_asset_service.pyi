from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.resources.types.asset_group_asset import AssetGroupAsset

_M = TypeVar("_M")

class AssetGroupAssetOperation(proto.Message):
    update_mask: FieldMask
    create: AssetGroupAsset
    update: AssetGroupAsset
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AssetGroupAsset = ...,
        update: AssetGroupAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetGroupAssetResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateAssetGroupAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetGroupAssetOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AssetGroupAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAssetGroupAssetsResponse(proto.Message):
    results: MutableSequence[MutateAssetGroupAssetResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAssetGroupAssetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
