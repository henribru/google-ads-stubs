from typing import Any

import proto

class KeywordPlanAdGroupKeywordErrorEnum(proto.Message):
    class KeywordPlanAdGroupKeywordError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_KEYWORD_MATCH_TYPE = 2
        DUPLICATE_KEYWORD = 3
        KEYWORD_TEXT_TOO_LONG = 4
        KEYWORD_HAS_INVALID_CHARS = 5
        KEYWORD_HAS_TOO_MANY_WORDS = 6
        INVALID_KEYWORD_TEXT = 7
        NEGATIVE_KEYWORD_HAS_CPC_BID = 8
        NEW_BMM_KEYWORDS_NOT_ALLOWED = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
