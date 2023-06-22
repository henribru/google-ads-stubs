from typing import Any

import proto

class GoogleAdsFieldCategoryEnum(proto.Message):
    class GoogleAdsFieldCategory(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESOURCE = 2
        ATTRIBUTE = 3
        SEGMENT = 5
        METRIC = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
