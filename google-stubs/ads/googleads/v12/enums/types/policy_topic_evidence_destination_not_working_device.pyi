from typing import Any

import proto

class PolicyTopicEvidenceDestinationNotWorkingDeviceEnum(proto.Message):
    class PolicyTopicEvidenceDestinationNotWorkingDevice(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DESKTOP = 2
        ANDROID = 3
        IOS = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
