from typing import Any

import proto

class MessagePlaceholderFieldEnum(proto.Message):
    class MessagePlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_NAME = 2
        COUNTRY_CODE = 3
        PHONE_NUMBER = 4
        MESSAGE_EXTENSION_TEXT = 5
        MESSAGE_TEXT = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
