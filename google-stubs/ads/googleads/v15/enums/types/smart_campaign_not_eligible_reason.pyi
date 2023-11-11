from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class SmartCampaignNotEligibleReasonEnum(proto.Message):
    class SmartCampaignNotEligibleReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCOUNT_ISSUE = 2
        BILLING_ISSUE = 3
        BUSINESS_PROFILE_LOCATION_REMOVED = 4
        ALL_ADS_DISAPPROVED = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
