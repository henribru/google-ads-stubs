from typing import Any

import proto

__protobuf__: Any

class FeedAttributeTypeEnum(proto.Message):
    class FeedAttributeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INT64: int
        DOUBLE: int
        STRING: int
        BOOLEAN: int
        URL: int
        DATE_TIME: int
        INT64_LIST: int
        DOUBLE_LIST: int
        STRING_LIST: int
        BOOLEAN_LIST: int
        URL_LIST: int
        DATE_TIME_LIST: int
        PRICE: int
