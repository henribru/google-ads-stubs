from typing import Any

import proto

__protobuf__: Any

class ValueRuleGeoLocationMatchTypeEnum(proto.Message):
    class ValueRuleGeoLocationMatchType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ANY: int
        LOCATION_OF_PRESENCE: int
