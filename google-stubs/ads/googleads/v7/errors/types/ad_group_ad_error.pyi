from typing import Any

import proto

__protobuf__: Any

class AdGroupAdErrorEnum(proto.Message):
    class AdGroupAdError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_GROUP_AD_LABEL_DOES_NOT_EXIST: int
        AD_GROUP_AD_LABEL_ALREADY_EXISTS: int
        AD_NOT_UNDER_ADGROUP: int
        CANNOT_OPERATE_ON_REMOVED_ADGROUPAD: int
        CANNOT_CREATE_DEPRECATED_ADS: int
        CANNOT_CREATE_TEXT_ADS: int
        EMPTY_FIELD: int
        RESOURCE_REFERENCED_IN_MULTIPLE_OPS: int
        AD_TYPE_CANNOT_BE_PAUSED: int
        AD_TYPE_CANNOT_BE_REMOVED: int
