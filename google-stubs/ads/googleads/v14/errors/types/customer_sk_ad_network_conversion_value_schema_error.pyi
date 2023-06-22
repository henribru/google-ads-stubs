from typing import Any

import proto

class CustomerSkAdNetworkConversionValueSchemaErrorEnum(proto.Message):
    class CustomerSkAdNetworkConversionValueSchemaError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_LINK_ID = 2
        INVALID_APP_ID = 3
        INVALID_SCHEMA = 4
        LINK_CODE_NOT_FOUND = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
