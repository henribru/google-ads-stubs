from typing import Any

import proto

class KeywordPlanKeywordAnnotationEnum(proto.Message):
    class KeywordPlanKeywordAnnotation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        KEYWORD_CONCEPT = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
