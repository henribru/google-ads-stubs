from typing import Any

import proto

__protobuf__: Any

class CriterionSystemServingStatusEnum(proto.Message):
    class CriterionSystemServingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ELIGIBLE: int
        RARELY_SERVED: int
