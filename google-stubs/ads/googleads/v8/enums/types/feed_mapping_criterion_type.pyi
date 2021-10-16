from typing import Any

import proto

__protobuf__: Any

class FeedMappingCriterionTypeEnum(proto.Message):
    class FeedMappingCriterionType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LOCATION_EXTENSION_TARGETING: int
        DSA_PAGE_FEED: int
