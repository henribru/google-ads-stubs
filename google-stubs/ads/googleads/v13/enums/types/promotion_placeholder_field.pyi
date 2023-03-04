from typing import Any

import proto

class PromotionPlaceholderFieldEnum(proto.Message):
    class PromotionPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PROMOTION_TARGET = 2
        DISCOUNT_MODIFIER = 3
        PERCENT_OFF = 4
        MONEY_AMOUNT_OFF = 5
        PROMOTION_CODE = 6
        ORDERS_OVER_AMOUNT = 7
        PROMOTION_START = 8
        PROMOTION_END = 9
        OCCASION = 10
        FINAL_URLS = 11
        FINAL_MOBILE_URLS = 12
        TRACKING_URL = 13
        LANGUAGE = 14
        FINAL_URL_SUFFIX = 15
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
