from typing import Any

import proto

class AdGroupCriterionCustomizerErrorEnum(proto.Message):
    class AdGroupCriterionCustomizerError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CRITERION_IS_NOT_KEYWORD = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
