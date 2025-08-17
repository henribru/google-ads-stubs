from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AttributionModelEnum(proto.Message):
    class AttributionModel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXTERNAL = 100
        GOOGLE_ADS_LAST_CLICK = 101
        GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK = 102
        GOOGLE_SEARCH_ATTRIBUTION_LINEAR = 103
        GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY = 104
        GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED = 105
        GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN = 106

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
