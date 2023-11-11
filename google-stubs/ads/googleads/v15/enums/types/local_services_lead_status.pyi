from typing import Any

import proto

class LocalServicesLeadStatusEnum(proto.Message):
    class LeadStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW = 2
        ACTIVE = 3
        BOOKED = 4
        DECLINED = 5
        EXPIRED = 6
        DISABLED = 7
        CONSUMER_DECLINED = 8
        WIPED_OUT = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
