from typing import Any

import proto

__protobuf__: Any

class BiddingSourceEnum(proto.Message):
    class BiddingSource(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN_BIDDING_STRATEGY: int
        AD_GROUP: int
        AD_GROUP_CRITERION: int
