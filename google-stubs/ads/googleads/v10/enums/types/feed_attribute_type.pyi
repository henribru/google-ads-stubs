from typing import Any

import proto

class FeedAttributeTypeEnum(proto.Message):
    class FeedAttributeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INT64 = 2
        DOUBLE = 3
        STRING = 4
        BOOLEAN = 5
        URL = 6
        DATE_TIME = 7
        INT64_LIST = 8
        DOUBLE_LIST = 9
        STRING_LIST = 10
        BOOLEAN_LIST = 11
        URL_LIST = 12
        DATE_TIME_LIST = 13
        PRICE = 14
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
