from typing import Any

import proto

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
