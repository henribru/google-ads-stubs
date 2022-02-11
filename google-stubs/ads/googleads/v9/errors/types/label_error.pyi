from typing import Any

import proto

__protobuf__: Any

class LabelErrorEnum(proto.Message):
    class LabelError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_APPLY_INACTIVE_LABEL: int
        CANNOT_APPLY_LABEL_TO_DISABLED_AD_GROUP_CRITERION: int
        CANNOT_APPLY_LABEL_TO_NEGATIVE_AD_GROUP_CRITERION: int
        EXCEEDED_LABEL_LIMIT_PER_TYPE: int
        INVALID_RESOURCE_FOR_MANAGER_LABEL: int
        DUPLICATE_NAME: int
        INVALID_LABEL_NAME: int
        CANNOT_ATTACH_LABEL_TO_DRAFT: int
        CANNOT_ATTACH_NON_MANAGER_LABEL_TO_CUSTOMER: int
