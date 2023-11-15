from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class PerformanceMaxUpgradeStatusEnum(proto.Message):
    class PerformanceMaxUpgradeStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UPGRADE_IN_PROGRESS = 3
        UPGRADE_COMPLETE = 4
        UPGRADE_FAILED = 5
        UPGRADE_ELIGIBLE = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
