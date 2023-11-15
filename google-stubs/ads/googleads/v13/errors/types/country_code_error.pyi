from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CountryCodeErrorEnum(proto.Message):
    class CountryCodeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_COUNTRY_CODE = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
