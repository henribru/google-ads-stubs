from typing import Any

import proto

class ShoppingAddProductsToCampaignRecommendationEnum(proto.Message):
    class Reason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS = 2
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS_IN_FEED = 3
        ADS_ACCOUNT_EXCLUDES_OFFERS_FROM_CAMPAIGN = 4
        ALL_PRODUCTS_ARE_EXCLUDED_FROM_CAMPAIGN = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
