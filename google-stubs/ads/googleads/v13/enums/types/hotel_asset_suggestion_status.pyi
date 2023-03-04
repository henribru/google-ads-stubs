from typing import Any

import proto

class HotelAssetSuggestionStatusEnum(proto.Message):
    class HotelAssetSuggestionStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SUCCESS = 2
        HOTEL_NOT_FOUND = 3
        INVALID_PLACE_ID = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
