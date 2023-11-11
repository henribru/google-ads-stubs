from typing import Any

import proto

class HotelDateSelectionTypeEnum(proto.Message):
    class HotelDateSelectionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEFAULT_SELECTION = 50
        USER_SELECTED = 51
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
