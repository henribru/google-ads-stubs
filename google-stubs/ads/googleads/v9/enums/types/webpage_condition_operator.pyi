from typing import Any

import proto

__protobuf__: Any

class WebpageConditionOperatorEnum(proto.Message):
    class WebpageConditionOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EQUALS: int
        CONTAINS: int
