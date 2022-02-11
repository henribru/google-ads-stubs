from typing import Any

import proto

__protobuf__: Any

class AccountLinkStatusEnum(proto.Message):
    class AccountLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        REQUESTED: int
        PENDING_APPROVAL: int
        REJECTED: int
        REVOKED: int
