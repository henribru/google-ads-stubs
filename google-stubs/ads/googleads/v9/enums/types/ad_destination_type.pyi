from typing import Any

import proto

__protobuf__: Any

class AdDestinationTypeEnum(proto.Message):
    class AdDestinationType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_APPLICABLE: int
        WEBSITE: int
        APP_DEEP_LINK: int
        APP_STORE: int
        PHONE_CALL: int
        MAP_DIRECTIONS: int
        LOCATION_LISTING: int
        MESSAGE: int
        LEAD_FORM: int
        YOUTUBE: int
        UNMODELED_FOR_CONVERSIONS: int
