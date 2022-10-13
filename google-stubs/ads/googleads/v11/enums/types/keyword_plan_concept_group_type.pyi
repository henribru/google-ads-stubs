from typing import Any

import proto

class KeywordPlanConceptGroupTypeEnum(proto.Message):
    class KeywordPlanConceptGroupType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BRAND = 2
        OTHER_BRANDS = 3
        NON_BRAND = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
