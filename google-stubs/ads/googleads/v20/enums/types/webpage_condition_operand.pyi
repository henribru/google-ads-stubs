import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class WebpageConditionOperandEnum(proto.Message):
    class WebpageConditionOperand(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        URL: int
        CATEGORY: int
        PAGE_TITLE: int
        PAGE_CONTENT: int
        CUSTOM_LABEL: int
