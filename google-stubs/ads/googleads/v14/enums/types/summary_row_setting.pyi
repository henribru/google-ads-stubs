from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class SummaryRowSettingEnum(proto.Message):
    class SummaryRowSetting(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_SUMMARY_ROW = 2
        SUMMARY_ROW_WITH_RESULTS = 3
        SUMMARY_ROW_ONLY = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
