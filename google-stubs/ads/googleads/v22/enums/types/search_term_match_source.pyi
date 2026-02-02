import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SearchTermMatchSourceEnum(proto.Message):
    class SearchTermMatchSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADVERTISER_PROVIDED_KEYWORD = 2
        AI_MAX_KEYWORDLESS = 3
        AI_MAX_BROAD_MATCH = 4
        DYNAMIC_SEARCH_ADS = 5
        PERFORMANCE_MAX = 6
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
