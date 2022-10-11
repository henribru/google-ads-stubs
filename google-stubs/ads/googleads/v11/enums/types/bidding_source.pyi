import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BiddingSourceEnum(proto.Message):
    class BiddingSource(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN_BIDDING_STRATEGY: int
        AD_GROUP: int
        AD_GROUP_CRITERION: int
