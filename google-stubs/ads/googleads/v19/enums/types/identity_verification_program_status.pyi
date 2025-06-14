import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class IdentityVerificationProgramStatusEnum(proto.Message):
    class IdentityVerificationProgramStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING_USER_ACTION = 2
        PENDING_REVIEW = 3
        SUCCESS = 4
        FAILURE = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
