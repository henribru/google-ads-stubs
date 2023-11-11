from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ShoppingAddProductsToCampaignRecommendationEnum(proto.Message):
    class Reason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS = 2
        MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS_IN_FEED = 3
        ADS_ACCOUNT_EXCLUDES_OFFERS_FROM_CAMPAIGN = 4
        ALL_PRODUCTS_ARE_EXCLUDED_FROM_CAMPAIGN = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
