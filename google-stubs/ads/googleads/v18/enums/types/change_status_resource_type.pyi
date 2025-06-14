import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ChangeStatusResourceTypeEnum(proto.Message):
    class ChangeStatusResourceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_GROUP: int
        AD_GROUP_AD: int
        AD_GROUP_CRITERION: int
        CAMPAIGN: int
        CAMPAIGN_CRITERION: int
        FEED: int
        FEED_ITEM: int
        AD_GROUP_FEED: int
        CAMPAIGN_FEED: int
        AD_GROUP_BID_MODIFIER: int
        SHARED_SET: int
        CAMPAIGN_SHARED_SET: int
        ASSET: int
        CUSTOMER_ASSET: int
        CAMPAIGN_ASSET: int
        AD_GROUP_ASSET: int
        COMBINED_AUDIENCE: int
        ASSET_GROUP: int
