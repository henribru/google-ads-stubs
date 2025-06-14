import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ShoppingAddProductsToCampaignRecommendationEnum(proto.Message):
    class Reason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS: int
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS_IN_FEED: int
        ADS_ACCOUNT_EXCLUDES_OFFERS_FROM_CAMPAIGN: int
        ALL_PRODUCTS_ARE_EXCLUDED_FROM_CAMPAIGN: int
