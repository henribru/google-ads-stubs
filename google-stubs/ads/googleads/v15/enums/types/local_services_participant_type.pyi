from typing import Any

import proto

class LocalServicesParticipantTypeEnum(proto.Message):
    class ParticipantType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADVERTISER = 2
        CONSUMER = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
