from typing import Any

import proto

class LeadFormPostSubmitCallToActionTypeEnum(proto.Message):
    class LeadFormPostSubmitCallToActionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        VISIT_SITE = 2
        DOWNLOAD = 3
        LEARN_MORE = 4
        SHOP_NOW = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
