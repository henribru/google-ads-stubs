from typing import Any

import proto

class CountryCodeErrorEnum(proto.Message):
    class CountryCodeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_COUNTRY_CODE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
