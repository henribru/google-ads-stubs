from typing import Any

import proto

__protobuf__: Any

class GoogleAdsFieldDataTypeEnum(proto.Message):
    class GoogleAdsFieldDataType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BOOLEAN: int
        DATE: int
        DOUBLE: int
        ENUM: int
        FLOAT: int
        INT32: int
        INT64: int
        MESSAGE: int
        RESOURCE_NAME: int
        STRING: int
        UINT64: int
