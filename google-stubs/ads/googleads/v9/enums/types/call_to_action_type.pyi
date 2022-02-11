from typing import Any

import proto

__protobuf__: Any

class CallToActionTypeEnum(proto.Message):
    class CallToActionType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LEARN_MORE: int
        GET_QUOTE: int
        APPLY_NOW: int
        SIGN_UP: int
        CONTACT_US: int
        SUBSCRIBE: int
        DOWNLOAD: int
        BOOK_NOW: int
        SHOP_NOW: int
