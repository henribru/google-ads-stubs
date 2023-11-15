from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ValueRuleOperationEnum(proto.Message):
    class ValueRuleOperation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADD = 2
        MULTIPLY = 3
        SET = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
