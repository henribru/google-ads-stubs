from typing import Any

import proto

__protobuf__: Any

class KeywordPlanAdGroupKeywordErrorEnum(proto.Message):
    class KeywordPlanAdGroupKeywordError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_KEYWORD_MATCH_TYPE: int
        DUPLICATE_KEYWORD: int
        KEYWORD_TEXT_TOO_LONG: int
        KEYWORD_HAS_INVALID_CHARS: int
        KEYWORD_HAS_TOO_MANY_WORDS: int
        INVALID_KEYWORD_TEXT: int
        NEGATIVE_KEYWORD_HAS_CPC_BID: int
        NEW_BMM_KEYWORDS_NOT_ALLOWED: int
