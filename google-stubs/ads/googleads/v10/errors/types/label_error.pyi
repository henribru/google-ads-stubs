from typing import Any

import proto

class LabelErrorEnum(proto.Message):
    class LabelError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_APPLY_INACTIVE_LABEL = 2
        CANNOT_APPLY_LABEL_TO_DISABLED_AD_GROUP_CRITERION = 3
        CANNOT_APPLY_LABEL_TO_NEGATIVE_AD_GROUP_CRITERION = 4
        EXCEEDED_LABEL_LIMIT_PER_TYPE = 5
        INVALID_RESOURCE_FOR_MANAGER_LABEL = 6
        DUPLICATE_NAME = 7
        INVALID_LABEL_NAME = 8
        CANNOT_ATTACH_LABEL_TO_DRAFT = 9
        CANNOT_ATTACH_NON_MANAGER_LABEL_TO_CUSTOMER = 10
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
