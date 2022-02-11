from typing import Any

import proto

__protobuf__: Any

class ConversionValueRulePrimaryDimensionEnum(proto.Message):
    class ConversionValueRulePrimaryDimension(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NO_RULE_APPLIED: int
        ORIGINAL: int
        NEW_VS_RETURNING_USER: int
        GEO_LOCATION: int
        DEVICE: int
        AUDIENCE: int
        MULTIPLE: int
