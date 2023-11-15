from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.bidding import (
    EnhancedCpc,
    MaximizeConversions,
    MaximizeConversionValue,
    TargetCpa,
    TargetImpressionShare,
    TargetRoas,
    TargetSpend,
)
from google.ads.googleads.v14.enums.types.bidding_strategy_status import (
    BiddingStrategyStatusEnum,
)
from google.ads.googleads.v14.enums.types.bidding_strategy_type import (
    BiddingStrategyTypeEnum,
)

_M = TypeVar("_M")

class BiddingStrategy(proto.Message):
    resource_name: str
    id: int
    name: str
    status: BiddingStrategyStatusEnum.BiddingStrategyStatus
    type_: BiddingStrategyTypeEnum.BiddingStrategyType
    currency_code: str
    effective_currency_code: str
    aligned_campaign_budget_id: int
    campaign_count: int
    non_removed_campaign_count: int
    enhanced_cpc: EnhancedCpc
    maximize_conversion_value: MaximizeConversionValue
    maximize_conversions: MaximizeConversions
    target_cpa: TargetCpa
    target_impression_share: TargetImpressionShare
    target_roas: TargetRoas
    target_spend: TargetSpend
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: BiddingStrategyStatusEnum.BiddingStrategyStatus = ...,
        type_: BiddingStrategyTypeEnum.BiddingStrategyType = ...,
        currency_code: str = ...,
        effective_currency_code: str = ...,
        aligned_campaign_budget_id: int = ...,
        campaign_count: int = ...,
        non_removed_campaign_count: int = ...,
        enhanced_cpc: EnhancedCpc = ...,
        maximize_conversion_value: MaximizeConversionValue = ...,
        maximize_conversions: MaximizeConversions = ...,
        target_cpa: TargetCpa = ...,
        target_impression_share: TargetImpressionShare = ...,
        target_roas: TargetRoas = ...,
        target_spend: TargetSpend = ...
    ) -> None: ...
