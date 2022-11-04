from typing import Any

import proto

class KeywordPlanCampaignKeywordErrorEnum(proto.Message):
    class KeywordPlanCampaignKeywordError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_KEYWORD_IS_POSITIVE = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
