from typing import Any

import proto

class AdGroupAdErrorEnum(proto.Message):
    class AdGroupAdError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_AD_LABEL_DOES_NOT_EXIST = 2
        AD_GROUP_AD_LABEL_ALREADY_EXISTS = 3
        AD_NOT_UNDER_ADGROUP = 4
        CANNOT_OPERATE_ON_REMOVED_ADGROUPAD = 5
        CANNOT_CREATE_DEPRECATED_ADS = 6
        CANNOT_CREATE_TEXT_ADS = 7
        EMPTY_FIELD = 8
        RESOURCE_REFERENCED_IN_MULTIPLE_OPS = 9
        AD_TYPE_CANNOT_BE_PAUSED = 10
        AD_TYPE_CANNOT_BE_REMOVED = 11
        CANNOT_UPDATE_DEPRECATED_ADS = 12
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
