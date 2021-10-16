from typing import Any

import proto

__protobuf__: Any

class AdCustomizerErrorEnum(proto.Message):
    class AdCustomizerError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        COUNTDOWN_INVALID_DATE_FORMAT: int
        COUNTDOWN_DATE_IN_PAST: int
        COUNTDOWN_INVALID_LOCALE: int
        COUNTDOWN_INVALID_START_DAYS_BEFORE: int
        UNKNOWN_USER_LIST: int
