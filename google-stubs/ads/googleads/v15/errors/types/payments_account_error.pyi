from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class PaymentsAccountErrorEnum(proto.Message):
    class PaymentsAccountError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_SUPPORTED_FOR_MANAGER_CUSTOMER = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
