import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ExtensionTypeEnum(proto.Message):
    class ExtensionType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NONE: int
        APP: int
        CALL: int
        CALLOUT: int
        MESSAGE: int
        PRICE: int
        PROMOTION: int
        SITELINK: int
        STRUCTURED_SNIPPET: int
        LOCATION: int
        AFFILIATE_LOCATION: int
        HOTEL_CALLOUT: int
        IMAGE: int
