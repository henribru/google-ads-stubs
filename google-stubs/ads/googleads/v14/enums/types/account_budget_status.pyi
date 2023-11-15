from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AccountBudgetStatusEnum(proto.Message):
    class AccountBudgetStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        APPROVED = 3
        CANCELLED = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
