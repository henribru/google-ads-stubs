from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AssetSetLinkErrorEnum(proto.Message):
    class AssetSetLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE = 2
        DUPLICATE_FEED_LINK = 3
        INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE = 4
        DUPLICATE_ASSET_SET_LINK = 5
        ASSET_SET_LINK_CANNOT_BE_REMOVED = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
