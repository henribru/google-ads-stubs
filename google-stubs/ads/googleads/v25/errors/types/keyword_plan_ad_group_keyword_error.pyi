from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
