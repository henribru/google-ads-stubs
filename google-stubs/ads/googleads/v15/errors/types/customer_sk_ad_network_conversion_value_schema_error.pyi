from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CustomerSkAdNetworkConversionValueSchemaErrorEnum(proto.Message):
    class CustomerSkAdNetworkConversionValueSchemaError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_LINK_ID = 2
        INVALID_APP_ID = 3
        INVALID_SCHEMA = 4
        LINK_CODE_NOT_FOUND = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
