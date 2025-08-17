import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetGroupProductGroupView(proto.Message):
    resource_name: str
    asset_group: str
    asset_group_listing_group_filter: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., asset_group: str = ..., asset_group_listing_group_filter: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "asset_group", "asset_group_listing_group_filter"]) -> bool: ...
