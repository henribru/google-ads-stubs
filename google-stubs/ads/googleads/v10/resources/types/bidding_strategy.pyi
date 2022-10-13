from typing import Any

import proto

from google.ads.googleads.v10.common.types.bidding import (
    EnhancedCpc,
    MaximizeConversions,
    MaximizeConversionValue,
    TargetCpa,
    TargetImpressionShare,
    TargetRoas,
    TargetSpend,
)
from google.ads.googleads.v10.enums.types.bidding_strategy_status import (
    BiddingStrategyStatusEnum,
)
from google.ads.googleads.v10.enums.types.bidding_strategy_type import (
    BiddingStrategyTypeEnum,
)

class BiddingStrategy(proto.Message):
    resource_name: str
    id: int
    name: str
    status: BiddingStrategyStatusEnum.BiddingStrategyStatus
    type_: BiddingStrategyTypeEnum.BiddingStrategyType
    currency_code: str
    effective_currency_code: str
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: BiddingStrategyStatusEnum.BiddingStrategyStatus = ...,
        type_: BiddingStrategyTypeEnum.BiddingStrategyType = ...,
        currency_code: str = ...,
        effective_currency_code: str = ...,
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
