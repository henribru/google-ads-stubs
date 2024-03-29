from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FeedItemQualityDisapprovalReasonEnum(proto.Message):
    class FeedItemQualityDisapprovalReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PRICE_TABLE_REPETITIVE_HEADERS = 2
        PRICE_TABLE_REPETITIVE_DESCRIPTION = 3
        PRICE_TABLE_INCONSISTENT_ROWS = 4
        PRICE_DESCRIPTION_HAS_PRICE_QUALIFIERS = 5
        PRICE_UNSUPPORTED_LANGUAGE = 6
        PRICE_TABLE_ROW_HEADER_TABLE_TYPE_MISMATCH = 7
        PRICE_TABLE_ROW_HEADER_HAS_PROMOTIONAL_TEXT = 8
        PRICE_TABLE_ROW_DESCRIPTION_NOT_RELEVANT = 9
        PRICE_TABLE_ROW_DESCRIPTION_HAS_PROMOTIONAL_TEXT = 10
        PRICE_TABLE_ROW_HEADER_DESCRIPTION_REPETITIVE = 11
        PRICE_TABLE_ROW_UNRATEABLE = 12
        PRICE_TABLE_ROW_PRICE_INVALID = 13
        PRICE_TABLE_ROW_URL_INVALID = 14
        PRICE_HEADER_OR_DESCRIPTION_HAS_PRICE = 15
        STRUCTURED_SNIPPETS_HEADER_POLICY_VIOLATED = 16
        STRUCTURED_SNIPPETS_REPEATED_VALUES = 17
        STRUCTURED_SNIPPETS_EDITORIAL_GUIDELINES = 18
        STRUCTURED_SNIPPETS_HAS_PROMOTIONAL_TEXT = 19

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
