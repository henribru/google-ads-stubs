from typing import Any

import proto

class CallToActionTypeEnum(proto.Message):
    class CallToActionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LEARN_MORE = 2
        GET_QUOTE = 3
        APPLY_NOW = 4
        SIGN_UP = 5
        CONTACT_US = 6
        SUBSCRIBE = 7
        DOWNLOAD = 8
        BOOK_NOW = 9
        SHOP_NOW = 10
        BUY_NOW = 11
        DONATE_NOW = 12
        ORDER_NOW = 13
        PLAY_NOW = 14
        SEE_MORE = 15
        START_NOW = 16
        VISIT_SITE = 17
        WATCH_NOW = 18
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
