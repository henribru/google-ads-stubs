import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import bidding
from google.ads.googleads.v19.enums.types import bidding_strategy_status, bidding_strategy_type

__protobuf__: Incomplete

class BiddingStrategy(proto.Message):
    resource_name: str
    id: int
    name: str
    status: bidding_strategy_status.BiddingStrategyStatusEnum.BiddingStrategyStatus
    type_: bidding_strategy_type.BiddingStrategyTypeEnum.BiddingStrategyType
    currency_code: str
    effective_currency_code: str
    aligned_campaign_budget_id: int
    campaign_count: int
    non_removed_campaign_count: int
    enhanced_cpc: bidding.EnhancedCpc
    maximize_conversion_value: bidding.MaximizeConversionValue
    maximize_conversions: bidding.MaximizeConversions
    target_cpa: bidding.TargetCpa
    target_impression_share: bidding.TargetImpressionShare
    target_roas: bidding.TargetRoas
    target_spend: bidding.TargetSpend
