from typing import Any

import proto

__protobuf__: Any

class GoogleVoiceCallStatusEnum(proto.Message):
    class GoogleVoiceCallStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MISSED: int
        RECEIVED: int
