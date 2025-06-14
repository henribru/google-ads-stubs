import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AccessRoleEnum(proto.Message):
    class AccessRole(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADMIN = 2
        STANDARD = 3
        READ_ONLY = 4
        EMAIL_ONLY = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
