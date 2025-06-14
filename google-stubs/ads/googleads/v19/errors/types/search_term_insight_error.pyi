import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SearchTermInsightErrorEnum(proto.Message):
    class SearchTermInsightError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FILTERING_NOT_ALLOWED_WITH_SEGMENTS: int
        LIMIT_NOT_ALLOWED_WITH_SEGMENTS: int
        MISSING_FIELD_IN_SELECT_CLAUSE: int
        REQUIRES_FILTER_BY_SINGLE_RESOURCE: int
        SORTING_NOT_ALLOWED_WITH_SEGMENTS: int
        SUMMARY_ROW_NOT_ALLOWED_WITH_SEGMENTS: int
