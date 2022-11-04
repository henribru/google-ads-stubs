from typing import Any

import proto

class ConversionActionCategoryEnum(proto.Message):
    class ConversionActionCategory(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEFAULT = 2
        PAGE_VIEW = 3
        PURCHASE = 4
        SIGNUP = 5
        DOWNLOAD = 7
        ADD_TO_CART = 8
        BEGIN_CHECKOUT = 9
        SUBSCRIBE_PAID = 10
        PHONE_CALL_LEAD = 11
        IMPORTED_LEAD = 12
        SUBMIT_LEAD_FORM = 13
        BOOK_APPOINTMENT = 14
        REQUEST_QUOTE = 15
        GET_DIRECTIONS = 16
        OUTBOUND_CLICK = 17
        CONTACT = 18
        ENGAGEMENT = 19
        STORE_VISIT = 20
        STORE_SALE = 21
        QUALIFIED_LEAD = 22
        CONVERTED_LEAD = 23
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
