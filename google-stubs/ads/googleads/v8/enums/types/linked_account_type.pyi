from typing import Any

import proto

__protobuf__: Any

class LinkedAccountTypeEnum(proto.Message):
    class LinkedAccountType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        THIRD_PARTY_APP_ANALYTICS: int
        DATA_PARTNER: int
        GOOGLE_ADS: int
