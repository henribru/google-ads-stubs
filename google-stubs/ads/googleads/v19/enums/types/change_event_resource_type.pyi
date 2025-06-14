import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ChangeEventResourceTypeEnum(proto.Message):
    class ChangeEventResourceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD: int
        AD_GROUP: int
        AD_GROUP_CRITERION: int
        CAMPAIGN: int
        CAMPAIGN_BUDGET: int
        AD_GROUP_BID_MODIFIER: int
        CAMPAIGN_CRITERION: int
        FEED: int
        FEED_ITEM: int
        CAMPAIGN_FEED: int
        AD_GROUP_FEED: int
        AD_GROUP_AD: int
        ASSET: int
        CUSTOMER_ASSET: int
        CAMPAIGN_ASSET: int
        AD_GROUP_ASSET: int
        ASSET_SET: int
        ASSET_SET_ASSET: int
        CAMPAIGN_ASSET_SET: int
