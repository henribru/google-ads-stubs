from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class UserListStringRuleItemOperatorEnum(proto.Message):
    class UserListStringRuleItemOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONTAINS = 2
        EQUALS = 3
        STARTS_WITH = 4
        ENDS_WITH = 5
        NOT_EQUALS = 6
        NOT_CONTAINS = 7
        NOT_STARTS_WITH = 8
        NOT_ENDS_WITH = 9

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
