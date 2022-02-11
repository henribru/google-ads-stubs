from typing import Any

import proto

__protobuf__: Any

class LocationExtensionTargetingCriterionFieldEnum(proto.Message):
    class LocationExtensionTargetingCriterionField(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADDRESS_LINE_1: int
        ADDRESS_LINE_2: int
        CITY: int
        PROVINCE: int
        POSTAL_CODE: int
        COUNTRY_CODE: int
