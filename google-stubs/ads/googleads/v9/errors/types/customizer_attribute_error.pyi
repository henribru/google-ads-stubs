from typing import Any

import proto

__protobuf__: Any

class CustomizerAttributeErrorEnum(proto.Message):
    class CustomizerAttributeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_CUSTOMIZER_ATTRIBUTE_NAME: int
