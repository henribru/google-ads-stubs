from typing import Any

import proto

class LocationExtensionTargetingCriterionFieldEnum(proto.Message):
    class LocationExtensionTargetingCriterionField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADDRESS_LINE_1 = 2
        ADDRESS_LINE_2 = 3
        CITY = 4
        PROVINCE = 5
        POSTAL_CODE = 6
        COUNTRY_CODE = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
