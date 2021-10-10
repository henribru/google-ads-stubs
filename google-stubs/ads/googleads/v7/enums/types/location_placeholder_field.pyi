from typing import Any

import proto

__protobuf__: Any

class LocationPlaceholderFieldEnum(proto.Message):
    class LocationPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BUSINESS_NAME: int
        ADDRESS_LINE_1: int
        ADDRESS_LINE_2: int
        CITY: int
        PROVINCE: int
        POSTAL_CODE: int
        COUNTRY_CODE: int
        PHONE_NUMBER: int
