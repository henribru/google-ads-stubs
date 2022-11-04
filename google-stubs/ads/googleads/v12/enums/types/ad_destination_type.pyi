from typing import Any

import proto

class AdDestinationTypeEnum(proto.Message):
    class AdDestinationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_APPLICABLE = 2
        WEBSITE = 3
        APP_DEEP_LINK = 4
        APP_STORE = 5
        PHONE_CALL = 6
        MAP_DIRECTIONS = 7
        LOCATION_LISTING = 8
        MESSAGE = 9
        LEAD_FORM = 10
        YOUTUBE = 11
        UNMODELED_FOR_CONVERSIONS = 12
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
