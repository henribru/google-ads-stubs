from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class QualityScoreBucketEnum(proto.Message):
    class QualityScoreBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BELOW_AVERAGE = 2
        AVERAGE = 3
        ABOVE_AVERAGE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(self, key: NoReturn) -> bool: ...  # type: ignore[override]
