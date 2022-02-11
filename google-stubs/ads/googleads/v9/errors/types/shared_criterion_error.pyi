from typing import Any

import proto

__protobuf__: Any

class SharedCriterionErrorEnum(proto.Message):
    class SharedCriterionError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE: int
