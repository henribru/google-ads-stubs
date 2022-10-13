from typing import Any

import proto

class CallPlaceholderFieldEnum(proto.Message):
    class CallPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PHONE_NUMBER = 2
        COUNTRY_CODE = 3
        TRACKED = 4
        CONVERSION_TYPE_ID = 5
        CONVERSION_REPORTING_STATE = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
