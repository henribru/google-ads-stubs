from typing import Any

import proto

class AssetGroupPrimaryStatusReasonEnum(proto.Message):
    class AssetGroupPrimaryStatusReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ASSET_GROUP_PAUSED = 2
        ASSET_GROUP_REMOVED = 3
        CAMPAIGN_REMOVED = 4
        CAMPAIGN_PAUSED = 5
        CAMPAIGN_PENDING = 6
        CAMPAIGN_ENDED = 7
        ASSET_GROUP_LIMITED = 8
        ASSET_GROUP_DISAPPROVED = 9
        ASSET_GROUP_UNDER_REVIEW = 10
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
