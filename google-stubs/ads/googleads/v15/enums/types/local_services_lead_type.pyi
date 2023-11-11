from typing import Any

import proto

class LocalServicesLeadTypeEnum(proto.Message):
    class LeadType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MESSAGE = 2
        PHONE_CALL = 3
        BOOKING = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
