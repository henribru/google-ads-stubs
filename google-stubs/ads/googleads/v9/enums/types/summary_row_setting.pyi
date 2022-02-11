from typing import Any

import proto

__protobuf__: Any

class SummaryRowSettingEnum(proto.Message):
    class SummaryRowSetting(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NO_SUMMARY_ROW: int
        SUMMARY_ROW_WITH_RESULTS: int
        SUMMARY_ROW_ONLY: int
