from typing import Any

import proto

__protobuf__: Any

class AssetSetLinkErrorEnum(proto.Message):
    class AssetSetLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE: int
        DUPLICATE_FEED_LINK: int
        INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE: int
        DUPLICATE_ASSET_SET_LINK: int
        ASSET_SET_LINK_CANNOT_BE_REMOVED: int
