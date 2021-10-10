from typing import Any

import proto

__protobuf__: Any

class ConversionAttributionEventTypeEnum(proto.Message):
    class ConversionAttributionEventType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        IMPRESSION: int
        INTERACTION: int
