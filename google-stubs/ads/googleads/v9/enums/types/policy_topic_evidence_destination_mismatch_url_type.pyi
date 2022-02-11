from typing import Any

import proto

__protobuf__: Any

class PolicyTopicEvidenceDestinationMismatchUrlTypeEnum(proto.Message):
    class PolicyTopicEvidenceDestinationMismatchUrlType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DISPLAY_URL: int
        FINAL_URL: int
        FINAL_MOBILE_URL: int
        TRACKING_URL: int
        MOBILE_TRACKING_URL: int
