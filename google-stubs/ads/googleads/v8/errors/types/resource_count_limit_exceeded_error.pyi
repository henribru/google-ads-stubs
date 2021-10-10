from typing import Any

import proto

__protobuf__: Any

class ResourceCountLimitExceededErrorEnum(proto.Message):
    class ResourceCountLimitExceededError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACCOUNT_LIMIT: int
        CAMPAIGN_LIMIT: int
        ADGROUP_LIMIT: int
        AD_GROUP_AD_LIMIT: int
        AD_GROUP_CRITERION_LIMIT: int
        SHARED_SET_LIMIT: int
        MATCHING_FUNCTION_LIMIT: int
        RESPONSE_ROW_LIMIT_EXCEEDED: int
        RESOURCE_LIMIT: int
