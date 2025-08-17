from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdGroupCriterionPrimaryStatusReasonEnum(proto.Message):
    class AdGroupCriterionPrimaryStatusReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_PENDING = 2
        CAMPAIGN_CRITERION_NEGATIVE = 3
        CAMPAIGN_PAUSED = 4
        CAMPAIGN_REMOVED = 5
        CAMPAIGN_ENDED = 6
        AD_GROUP_PAUSED = 7
        AD_GROUP_REMOVED = 8
        AD_GROUP_CRITERION_DISAPPROVED = 9
        AD_GROUP_CRITERION_RARELY_SERVED = 10
        AD_GROUP_CRITERION_LOW_QUALITY = 11
        AD_GROUP_CRITERION_UNDER_REVIEW = 12
        AD_GROUP_CRITERION_PENDING_REVIEW = 13
        AD_GROUP_CRITERION_BELOW_FIRST_PAGE_BID = 14
        AD_GROUP_CRITERION_NEGATIVE = 15
        AD_GROUP_CRITERION_RESTRICTED = 16
        AD_GROUP_CRITERION_PAUSED = 17
        AD_GROUP_CRITERION_PAUSED_DUE_TO_LOW_ACTIVITY = 18
        AD_GROUP_CRITERION_REMOVED = 19

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
