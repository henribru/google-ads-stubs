from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PolicyTopicEntryTypeEnum(proto.Message):
    class PolicyTopicEntryType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PROHIBITED = 2
        LIMITED = 4
        FULLY_LIMITED = 8
        DESCRIPTIVE = 5
        BROADENING = 6
        AREA_OF_INTEREST_ONLY = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
