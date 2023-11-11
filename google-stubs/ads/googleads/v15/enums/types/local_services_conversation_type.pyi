from typing import Any

import proto

class LocalServicesLeadConversationTypeEnum(proto.Message):
    class ConversationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMAIL = 2
        MESSAGE = 3
        PHONE_CALL = 4
        SMS = 5
        BOOKING = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
