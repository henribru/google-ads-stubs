import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class PerformanceMaxUpgradeStatusEnum(proto.Message):
    class PerformanceMaxUpgradeStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UPGRADE_IN_PROGRESS = 3
        UPGRADE_COMPLETE = 4
        UPGRADE_FAILED = 5
        UPGRADE_ELIGIBLE = 6
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
