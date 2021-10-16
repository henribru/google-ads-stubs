from typing import Any

import proto

__protobuf__: Any

class RegionCodeErrorEnum(proto.Message):
    class RegionCodeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_REGION_CODE: int
