from typing import Any

import proto

class ConversionOriginEnum(proto.Message):
    class ConversionOrigin(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WEBSITE = 2
        GOOGLE_HOSTED = 3
        APP = 4
        CALL_FROM_ADS = 5
        STORE = 6
        YOUTUBE_HOSTED = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
