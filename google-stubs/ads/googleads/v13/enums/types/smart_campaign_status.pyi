from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class SmartCampaignStatusEnum(proto.Message):
    class SmartCampaignStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAUSED = 2
        NOT_ELIGIBLE = 3
        PENDING = 4
        ELIGIBLE = 5
        REMOVED = 6
        ENDED = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
