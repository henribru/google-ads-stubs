from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class FrequencyCapLevelEnum(proto.Message):
    class FrequencyCapLevel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_AD = 2
        AD_GROUP = 3
        CAMPAIGN = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
