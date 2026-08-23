from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SurveyIntendedActionEnum(proto.Message):
    class SurveyIntendedAction(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPLY_FOR = 2
        APPLY_TO_WORK_FOR = 3
        ATTEND = 4
        BOOK = 5
        BOOK_WITH = 6
        BUY = 7
        BUY_CONTENT_FROM = 8
        BUY_TICKETS_FOR = 9
        CARE_ABOUT = 10
        CHOOSE = 11
        DONATE_TO = 12
        DOWNLOAD = 13
        DOWNLOAD_FROM = 14
        EAT = 15
        EAT_AT = 16
        HAVE_UNFAVORABLE_OPINION_OF = 17
        JOIN = 18
        LEARN = 19
        LISTEN_TO = 20
        NONE = 21
        ORDER_FROM = 22
        PARTICIPATE_IN = 23
        PLAY = 24
        PLAY_AT = 25
        PLAY_ON = 26
        RENT = 27
        SEE = 28
        SEE_IN_THEATERS = 29
        SHOP = 30
        SIGN_UP_FOR = 31
        SUBSCRIBE_TO = 32
        TAKE_ACTION_ON = 33
        USE = 34
        VISIT = 35
        VOTE_FOR = 36
        WATCH = 37
        WATCH_IN_THEATERS = 38

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
