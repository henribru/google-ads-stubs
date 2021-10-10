from typing import Any

import proto

__protobuf__: Any

class PlaceholderTypeEnum(proto.Message):
    class PlaceholderType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SITELINK: int
        CALL: int
        APP: int
        LOCATION: int
        AFFILIATE_LOCATION: int
        CALLOUT: int
        STRUCTURED_SNIPPET: int
        MESSAGE: int
        PRICE: int
        PROMOTION: int
        AD_CUSTOMIZER: int
        DYNAMIC_EDUCATION: int
        DYNAMIC_FLIGHT: int
        DYNAMIC_CUSTOM: int
        DYNAMIC_HOTEL: int
        DYNAMIC_REAL_ESTATE: int
        DYNAMIC_TRAVEL: int
        DYNAMIC_LOCAL: int
        DYNAMIC_JOB: int
        IMAGE: int
