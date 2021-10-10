from typing import Any

import proto

__protobuf__: Any

class HotelDateSelectionTypeEnum(proto.Message):
    class HotelDateSelectionType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DEFAULT_SELECTION: int
        USER_SELECTED: int
