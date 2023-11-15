from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AssetAutomationStatusEnum(proto.Message):
    class AssetAutomationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPTED_IN = 2
        OPTED_OUT = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
