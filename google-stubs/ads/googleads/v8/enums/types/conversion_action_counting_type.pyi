from typing import Any

import proto

__protobuf__: Any

class ConversionActionCountingTypeEnum(proto.Message):
    class ConversionActionCountingType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ONE_PER_CLICK: int
        MANY_PER_CLICK: int
