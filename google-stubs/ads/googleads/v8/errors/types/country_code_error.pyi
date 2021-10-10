from typing import Any

import proto

__protobuf__: Any

class CountryCodeErrorEnum(proto.Message):
    class CountryCodeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_COUNTRY_CODE: int
