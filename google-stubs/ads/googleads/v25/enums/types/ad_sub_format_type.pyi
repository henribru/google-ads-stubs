from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdSubFormatTypeEnum(proto.Message):
    class AdSubFormatType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNSEGMENTED = 2
        INSTREAM_NON_SKIPPABLE_STANDARD = 3
        INSTREAM_NON_SKIPPABLE_MAX30_SEC = 4
        INSTREAM_NON_SKIPPABLE_MAX60_SEC = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
