import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerErrorEnum(proto.Message):
    class CustomerError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STATUS_CHANGE_DISALLOWED = 2
        ACCOUNT_NOT_SET_UP = 3
        CREATION_DENIED_FOR_POLICY_VIOLATION = 4
        CREATION_DENIED_INELIGIBLE_MCC = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
