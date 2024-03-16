from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
