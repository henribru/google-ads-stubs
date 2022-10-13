from typing import Any

import proto

class PolicyTopicEvidenceDestinationMismatchUrlTypeEnum(proto.Message):
    class PolicyTopicEvidenceDestinationMismatchUrlType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DISPLAY_URL = 2
        FINAL_URL = 3
        FINAL_MOBILE_URL = 4
        TRACKING_URL = 5
        MOBILE_TRACKING_URL = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
