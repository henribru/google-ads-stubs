from typing import Any

import proto

__protobuf__: Any

class PolicyTopicEntryTypeEnum(proto.Message):
    class PolicyTopicEntryType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PROHIBITED: int
        LIMITED: int
        FULLY_LIMITED: int
        DESCRIPTIVE: int
        BROADENING: int
        AREA_OF_INTEREST_ONLY: int
