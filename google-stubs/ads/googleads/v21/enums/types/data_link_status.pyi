import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class DataLinkStatusEnum(proto.Message):
    class DataLinkStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUESTED = 2
        PENDING_APPROVAL = 3
        ENABLED = 4
        DISABLED = 5
        REVOKED = 6
        REJECTED = 7
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
