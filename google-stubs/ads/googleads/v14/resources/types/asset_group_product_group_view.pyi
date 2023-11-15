from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AssetGroupProductGroupView(proto.Message):
    resource_name: str
    asset_group: str
    asset_group_listing_group_filter: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group: str = ...,
        asset_group_listing_group_filter: str = ...
    ) -> None: ...
