from typing import Any

import proto

class LocationPlaceholderFieldEnum(proto.Message):
    class LocationPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_NAME = 2
        ADDRESS_LINE_1 = 3
        ADDRESS_LINE_2 = 4
        CITY = 5
        PROVINCE = 6
        POSTAL_CODE = 7
        COUNTRY_CODE = 8
        PHONE_NUMBER = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
