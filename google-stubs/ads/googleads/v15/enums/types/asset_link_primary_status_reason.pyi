from typing import Any

import proto

class AssetLinkPrimaryStatusReasonEnum(proto.Message):
    class AssetLinkPrimaryStatusReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ASSET_LINK_PAUSED = 2
        ASSET_LINK_REMOVED = 3
        ASSET_DISAPPROVED = 4
        ASSET_UNDER_REVIEW = 5
        ASSET_APPROVED_LABELED = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
