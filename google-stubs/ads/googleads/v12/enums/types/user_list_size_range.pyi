from typing import Any

import proto

class UserListSizeRangeEnum(proto.Message):
    class UserListSizeRange(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LESS_THAN_FIVE_HUNDRED = 2
        LESS_THAN_ONE_THOUSAND = 3
        ONE_THOUSAND_TO_TEN_THOUSAND = 4
        TEN_THOUSAND_TO_FIFTY_THOUSAND = 5
        FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND = 6
        ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND = 7
        THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND = 8
        FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION = 9
        ONE_MILLION_TO_TWO_MILLION = 10
        TWO_MILLION_TO_THREE_MILLION = 11
        THREE_MILLION_TO_FIVE_MILLION = 12
        FIVE_MILLION_TO_TEN_MILLION = 13
        TEN_MILLION_TO_TWENTY_MILLION = 14
        TWENTY_MILLION_TO_THIRTY_MILLION = 15
        THIRTY_MILLION_TO_FIFTY_MILLION = 16
        OVER_FIFTY_MILLION = 17
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
