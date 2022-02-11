from typing import Any

import proto

__protobuf__: Any

class PromotionPlaceholderFieldEnum(proto.Message):
    class PromotionPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PROMOTION_TARGET: int
        DISCOUNT_MODIFIER: int
        PERCENT_OFF: int
        MONEY_AMOUNT_OFF: int
        PROMOTION_CODE: int
        ORDERS_OVER_AMOUNT: int
        PROMOTION_START: int
        PROMOTION_END: int
        OCCASION: int
        FINAL_URLS: int
        FINAL_MOBILE_URLS: int
        TRACKING_URL: int
        LANGUAGE: int
        FINAL_URL_SUFFIX: int
