from typing import Any

import proto

__protobuf__: Any

class PriceExtensionPriceQualifierEnum(proto.Message):
    class PriceExtensionPriceQualifier(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FROM: int
        UP_TO: int
        AVERAGE: int
