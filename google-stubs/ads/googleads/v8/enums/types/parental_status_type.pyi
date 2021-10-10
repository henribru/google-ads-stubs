from typing import Any

import proto

__protobuf__: Any

class ParentalStatusTypeEnum(proto.Message):
    class ParentalStatusType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PARENT: int
        NOT_A_PARENT: int
        UNDETERMINED: int
