from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v23.resources.types.asset_set_asset import AssetSetAsset
from google.ads.googleads.v23.resources.types.asset_set_asset import AssetSetAsset
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetSetAssetOperation(proto.Message):
    create: AssetSetAsset
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, create: AssetSetAsset = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
class MutateAssetSetAssetResult(proto.Message):
    resource_name: str
    asset_set_asset: AssetSetAsset
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., asset_set_asset: AssetSetAsset = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "asset_set_asset"]) -> bool: ...
class MutateAssetSetAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetSetAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[AssetSetAssetOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateAssetSetAssetsResponse(proto.Message):
    results: MutableSequence[MutateAssetSetAssetResult]
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, results: MutableSequence[MutateAssetSetAssetResult] = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results", "partial_failure_error"]) -> bool: ...
