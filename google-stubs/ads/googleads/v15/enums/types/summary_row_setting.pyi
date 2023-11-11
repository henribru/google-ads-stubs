from typing import Any

import proto

class SummaryRowSettingEnum(proto.Message):
    class SummaryRowSetting(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_SUMMARY_ROW = 2
        SUMMARY_ROW_WITH_RESULTS = 3
        SUMMARY_ROW_ONLY = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
