from typing import Any

import proto

__protobuf__: Any

class CallPlaceholderFieldEnum(proto.Message):
    class CallPlaceholderField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PHONE_NUMBER: int
        COUNTRY_CODE: int
        TRACKED: int
        CONVERSION_TYPE_ID: int
        CONVERSION_REPORTING_STATE: int
