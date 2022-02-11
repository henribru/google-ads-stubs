from typing import Any

import proto

__protobuf__: Any

class ListingGroupFilterTypeEnum(proto.Message):
    class ListingGroupFilterType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SUBDIVISION: int
        UNIT_INCLUDED: int
        UNIT_EXCLUDED: int
