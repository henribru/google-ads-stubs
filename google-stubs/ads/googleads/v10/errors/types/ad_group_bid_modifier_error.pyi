from typing import Any

import proto

class AdGroupBidModifierErrorEnum(proto.Message):
    class AdGroupBidModifierError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CRITERION_ID_NOT_SUPPORTED = 2
        CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
