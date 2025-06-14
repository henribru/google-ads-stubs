import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class UserListDateRuleItemOperatorEnum(proto.Message):
    class UserListDateRuleItemOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EQUALS = 2
        NOT_EQUALS = 3
        BEFORE = 4
        AFTER = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
