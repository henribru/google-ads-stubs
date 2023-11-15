from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class KeywordPlanAggregateMetricTypeEnum(proto.Message):
    class KeywordPlanAggregateMetricType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEVICE = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
