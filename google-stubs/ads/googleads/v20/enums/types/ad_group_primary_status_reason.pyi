import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupPrimaryStatusReasonEnum(proto.Message):
    class AdGroupPrimaryStatusReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_REMOVED = 2
        CAMPAIGN_PAUSED = 3
        CAMPAIGN_PENDING = 4
        CAMPAIGN_ENDED = 5
        AD_GROUP_PAUSED = 6
        AD_GROUP_REMOVED = 7
        AD_GROUP_INCOMPLETE = 8
        KEYWORDS_PAUSED = 9
        NO_KEYWORDS = 10
        AD_GROUP_ADS_PAUSED = 11
        NO_AD_GROUP_ADS = 12
        HAS_ADS_DISAPPROVED = 13
        HAS_ADS_LIMITED_BY_POLICY = 14
        MOST_ADS_UNDER_REVIEW = 15
        CAMPAIGN_DRAFT = 16
        AD_GROUP_PAUSED_DUE_TO_LOW_ACTIVITY = 19
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
