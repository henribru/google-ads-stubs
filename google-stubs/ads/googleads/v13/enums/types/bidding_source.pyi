from typing import Any

import proto

class BiddingSourceEnum(proto.Message):
    class BiddingSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_BIDDING_STRATEGY = 5
        AD_GROUP = 6
        AD_GROUP_CRITERION = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
