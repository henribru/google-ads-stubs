from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SearchTermInsightErrorEnum(proto.Message):
    class SearchTermInsightError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FILTERING_NOT_ALLOWED_WITH_SEGMENTS = 2
        LIMIT_NOT_ALLOWED_WITH_SEGMENTS = 3
        MISSING_FIELD_IN_SELECT_CLAUSE = 4
        REQUIRES_FILTER_BY_SINGLE_RESOURCE = 5
        SORTING_NOT_ALLOWED_WITH_SEGMENTS = 6
        SUMMARY_ROW_NOT_ALLOWED_WITH_SEGMENTS = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
