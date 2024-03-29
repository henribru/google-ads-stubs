from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PricePlaceholderFieldEnum(proto.Message):
    class PricePlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TYPE = 2
        PRICE_QUALIFIER = 3
        TRACKING_TEMPLATE = 4
        LANGUAGE = 5
        FINAL_URL_SUFFIX = 6
        ITEM_1_HEADER = 100
        ITEM_1_DESCRIPTION = 101
        ITEM_1_PRICE = 102
        ITEM_1_UNIT = 103
        ITEM_1_FINAL_URLS = 104
        ITEM_1_FINAL_MOBILE_URLS = 105
        ITEM_2_HEADER = 200
        ITEM_2_DESCRIPTION = 201
        ITEM_2_PRICE = 202
        ITEM_2_UNIT = 203
        ITEM_2_FINAL_URLS = 204
        ITEM_2_FINAL_MOBILE_URLS = 205
        ITEM_3_HEADER = 300
        ITEM_3_DESCRIPTION = 301
        ITEM_3_PRICE = 302
        ITEM_3_UNIT = 303
        ITEM_3_FINAL_URLS = 304
        ITEM_3_FINAL_MOBILE_URLS = 305
        ITEM_4_HEADER = 400
        ITEM_4_DESCRIPTION = 401
        ITEM_4_PRICE = 402
        ITEM_4_UNIT = 403
        ITEM_4_FINAL_URLS = 404
        ITEM_4_FINAL_MOBILE_URLS = 405
        ITEM_5_HEADER = 500
        ITEM_5_DESCRIPTION = 501
        ITEM_5_PRICE = 502
        ITEM_5_UNIT = 503
        ITEM_5_FINAL_URLS = 504
        ITEM_5_FINAL_MOBILE_URLS = 505
        ITEM_6_HEADER = 600
        ITEM_6_DESCRIPTION = 601
        ITEM_6_PRICE = 602
        ITEM_6_UNIT = 603
        ITEM_6_FINAL_URLS = 604
        ITEM_6_FINAL_MOBILE_URLS = 605
        ITEM_7_HEADER = 700
        ITEM_7_DESCRIPTION = 701
        ITEM_7_PRICE = 702
        ITEM_7_UNIT = 703
        ITEM_7_FINAL_URLS = 704
        ITEM_7_FINAL_MOBILE_URLS = 705
        ITEM_8_HEADER = 800
        ITEM_8_DESCRIPTION = 801
        ITEM_8_PRICE = 802
        ITEM_8_UNIT = 803
        ITEM_8_FINAL_URLS = 804
        ITEM_8_FINAL_MOBILE_URLS = 805

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
