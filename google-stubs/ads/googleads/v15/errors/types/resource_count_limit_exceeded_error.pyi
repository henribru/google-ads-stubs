from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ResourceCountLimitExceededErrorEnum(proto.Message):
    class ResourceCountLimitExceededError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCOUNT_LIMIT = 2
        CAMPAIGN_LIMIT = 3
        ADGROUP_LIMIT = 4
        AD_GROUP_AD_LIMIT = 5
        AD_GROUP_CRITERION_LIMIT = 6
        SHARED_SET_LIMIT = 7
        MATCHING_FUNCTION_LIMIT = 8
        RESPONSE_ROW_LIMIT_EXCEEDED = 9
        RESOURCE_LIMIT = 10
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
