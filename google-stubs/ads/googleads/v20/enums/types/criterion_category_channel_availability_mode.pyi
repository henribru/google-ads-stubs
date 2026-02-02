from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CriterionCategoryChannelAvailabilityModeEnum(proto.Message):
    class CriterionCategoryChannelAvailabilityMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_CHANNELS = 2
        CHANNEL_TYPE_AND_ALL_SUBTYPES = 3
        CHANNEL_TYPE_AND_SUBSET_SUBTYPES = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
