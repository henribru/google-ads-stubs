from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class UserListNumberRuleItemOperatorEnum(proto.Message):
    class UserListNumberRuleItemOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GREATER_THAN = 2
        GREATER_THAN_OR_EQUAL = 3
        EQUALS = 4
        NOT_EQUALS = 5
        LESS_THAN = 6
        LESS_THAN_OR_EQUAL = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
