import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomAudienceTypeEnum(proto.Message):
    class CustomAudienceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AUTO: int
        INTEREST: int
        PURCHASE_INTENT: int
        SEARCH: int
