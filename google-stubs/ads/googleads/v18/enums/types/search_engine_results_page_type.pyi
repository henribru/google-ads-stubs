import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SearchEngineResultsPageTypeEnum(proto.Message):
    class SearchEngineResultsPageType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADS_ONLY = 2
        ORGANIC_ONLY = 3
        ADS_AND_ORGANIC = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
