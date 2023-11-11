from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdCustomizerErrorEnum(proto.Message):
    class AdCustomizerError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        COUNTDOWN_INVALID_DATE_FORMAT = 2
        COUNTDOWN_DATE_IN_PAST = 3
        COUNTDOWN_INVALID_LOCALE = 4
        COUNTDOWN_INVALID_START_DAYS_BEFORE = 5
        UNKNOWN_USER_LIST = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
