from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.asset_group_asset import AssetGroupAsset

class AssetGroupAssetOperation(proto.Message):
    update_mask: FieldMask
    create: AssetGroupAsset
    update: AssetGroupAsset
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AssetGroupAsset = ...,
        update: AssetGroupAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetGroupAssetResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAssetGroupAssetsRequest(proto.Message):
    customer_id: str
    operations: list[AssetGroupAssetOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AssetGroupAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAssetGroupAssetsResponse(proto.Message):
    results: list[MutateAssetGroupAssetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAssetGroupAssetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
