from typing import Any

import proto

__protobuf__: Any

class UserInterestTaxonomyTypeEnum(proto.Message):
    class UserInterestTaxonomyType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AFFINITY: int
        IN_MARKET: int
        MOBILE_APP_INSTALL_USER: int
        VERTICAL_GEO: int
        NEW_SMART_PHONE_USER: int
