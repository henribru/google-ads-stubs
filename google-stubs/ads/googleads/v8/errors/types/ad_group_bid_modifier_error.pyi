from typing import Any

import proto

__protobuf__: Any

class AdGroupBidModifierErrorEnum(proto.Message):
    class AdGroupBidModifierError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CRITERION_ID_NOT_SUPPORTED: int
        CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER: int
