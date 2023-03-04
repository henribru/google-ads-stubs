from typing import Any

import proto

class DsaPageFeedCriterionFieldEnum(proto.Message):
    class DsaPageFeedCriterionField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAGE_URL = 2
        LABEL = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
