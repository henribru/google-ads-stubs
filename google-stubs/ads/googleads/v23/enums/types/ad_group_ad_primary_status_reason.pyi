from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdGroupAdPrimaryStatusReasonEnum(proto.Message):
    class AdGroupAdPrimaryStatusReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_REMOVED = 2
        CAMPAIGN_PAUSED = 3
        CAMPAIGN_PENDING = 4
        CAMPAIGN_ENDED = 5
        AD_GROUP_PAUSED = 6
        AD_GROUP_REMOVED = 7
        AD_GROUP_AD_PAUSED = 8
        AD_GROUP_AD_REMOVED = 9
        AD_GROUP_AD_DISAPPROVED = 10
        AD_GROUP_AD_UNDER_REVIEW = 11
        AD_GROUP_AD_POOR_QUALITY = 12
        AD_GROUP_AD_NO_ADS = 13
        AD_GROUP_AD_APPROVED_LABELED = 14
        AD_GROUP_AD_AREA_OF_INTEREST_ONLY = 15
        AD_GROUP_AD_UNDER_APPEAL = 16

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
