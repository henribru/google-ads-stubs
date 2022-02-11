from typing import Any

import proto

__protobuf__: Any

class LeadFormDesiredIntentEnum(proto.Message):
    class LeadFormDesiredIntent(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LOW_INTENT: int
        HIGH_INTENT: int
