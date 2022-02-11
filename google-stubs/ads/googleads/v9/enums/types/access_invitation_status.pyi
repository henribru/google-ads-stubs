from typing import Any

import proto

__protobuf__: Any

class AccessInvitationStatusEnum(proto.Message):
    class AccessInvitationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        DECLINED: int
        EXPIRED: int
