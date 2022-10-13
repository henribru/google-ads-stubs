from typing import Any

import proto

class LinkedAccountTypeEnum(proto.Message):
    class LinkedAccountType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        THIRD_PARTY_APP_ANALYTICS = 2
        DATA_PARTNER = 3
        GOOGLE_ADS = 4
        HOTEL_CENTER = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
