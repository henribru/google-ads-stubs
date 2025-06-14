import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class UserListLogicalRuleOperatorEnum(proto.Message):
    class UserListLogicalRuleOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL = 2
        ANY = 3
        NONE = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
