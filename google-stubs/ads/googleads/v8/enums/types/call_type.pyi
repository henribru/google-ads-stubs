from typing import Any

import proto

__protobuf__: Any

class CallTypeEnum(proto.Message):
    class CallType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MANUALLY_DIALED: int
        HIGH_END_MOBILE_SEARCH: int
