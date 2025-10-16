from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.asset_usage import AssetUsage
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupAdAssetCombinationView(proto.Message):
    resource_name: str
    served_assets: MutableSequence[AssetUsage]
    enabled: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., served_assets: MutableSequence[AssetUsage] = ..., enabled: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "served_assets", "enabled"]) -> bool: ...
