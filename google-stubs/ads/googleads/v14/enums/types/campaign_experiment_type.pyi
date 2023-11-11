from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CampaignExperimentTypeEnum(proto.Message):
    class CampaignExperimentType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BASE = 2
        DRAFT = 3
        EXPERIMENT = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
