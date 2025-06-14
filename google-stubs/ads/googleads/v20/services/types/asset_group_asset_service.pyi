from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.asset_group_asset import AssetGroupAsset
from google.ads.googleads.v20.resources.types.asset_group_asset import AssetGroupAsset
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetGroupAssetOperation(proto.Message):
    update_mask: FieldMask
    create: AssetGroupAsset
    update: AssetGroupAsset
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., create: AssetGroupAsset = ..., update: AssetGroupAsset = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateAssetGroupAssetResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateAssetGroupAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetGroupAssetOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[AssetGroupAssetOperation] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only"]) -> bool: ...
class MutateAssetGroupAssetsResponse(proto.Message):
    results: MutableSequence[MutateAssetGroupAssetResult]
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., results: MutableSequence[MutateAssetGroupAssetResult] = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results", "partial_failure_error"]) -> bool: ...
