from typing import Any

import proto

__protobuf__: Any

class BiddingStrategyTypeEnum(proto.Message):
    class BiddingStrategyType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        COMMISSION: int
        ENHANCED_CPC: int
        INVALID: int
        MANUAL_CPC: int
        MANUAL_CPM: int
        MANUAL_CPV: int
        MAXIMIZE_CONVERSIONS: int
        MAXIMIZE_CONVERSION_VALUE: int
        PAGE_ONE_PROMOTED: int
        PERCENT_CPC: int
        TARGET_CPA: int
        TARGET_CPM: int
        TARGET_IMPRESSION_SHARE: int
        TARGET_OUTRANK_SHARE: int
        TARGET_ROAS: int
        TARGET_SPEND: int
