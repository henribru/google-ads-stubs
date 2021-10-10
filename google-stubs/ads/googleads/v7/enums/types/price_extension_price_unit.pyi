from typing import Any

import proto

__protobuf__: Any

class PriceExtensionPriceUnitEnum(proto.Message):
    class PriceExtensionPriceUnit(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PER_HOUR: int
        PER_DAY: int
        PER_WEEK: int
        PER_MONTH: int
        PER_YEAR: int
        PER_NIGHT: int
