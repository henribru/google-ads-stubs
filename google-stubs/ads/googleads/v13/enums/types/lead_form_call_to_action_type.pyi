from typing import Any

import proto

class LeadFormCallToActionTypeEnum(proto.Message):
    class LeadFormCallToActionType(proto.Enum):
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
        GET_OFFER = 10
        REGISTER = 11
        GET_INFO = 12
        REQUEST_DEMO = 13
        JOIN_NOW = 14
        GET_STARTED = 15
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
