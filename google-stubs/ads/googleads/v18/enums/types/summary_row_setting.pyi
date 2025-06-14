import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SummaryRowSettingEnum(proto.Message):
    class SummaryRowSetting(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_SUMMARY_ROW = 2
        SUMMARY_ROW_WITH_RESULTS = 3
        SUMMARY_ROW_ONLY = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
