from typing import Any

import proto

__protobuf__: Any

class MessagePlaceholderFieldEnum(proto.Message):
    class MessagePlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BUSINESS_NAME: int
        COUNTRY_CODE: int
        PHONE_NUMBER: int
        MESSAGE_EXTENSION_TEXT: int
        MESSAGE_TEXT: int
