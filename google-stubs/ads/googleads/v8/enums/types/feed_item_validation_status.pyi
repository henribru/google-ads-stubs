from typing import Any

import proto

__protobuf__: Any

class FeedItemValidationStatusEnum(proto.Message):
    class FeedItemValidationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        INVALID: int
        VALID: int
