from typing import Any

import proto

__protobuf__: Any

class GenderTypeEnum(proto.Message):
    class GenderType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MALE: int
        FEMALE: int
        UNDETERMINED: int
