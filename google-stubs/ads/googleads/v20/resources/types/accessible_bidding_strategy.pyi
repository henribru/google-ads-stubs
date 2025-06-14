import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import bidding_strategy_type, target_impression_share_location

__protobuf__: Incomplete

class AccessibleBiddingStrategy(proto.Message):
    class MaximizeConversionValue(proto.Message):
        target_roas: float
    class MaximizeConversions(proto.Message):
        target_cpa_micros: int
    class TargetCpa(proto.Message):
        target_cpa_micros: int
    class TargetImpressionShare(proto.Message):
        location: target_impression_share_location.TargetImpressionShareLocationEnum.TargetImpressionShareLocation
        location_fraction_micros: int
        cpc_bid_ceiling_micros: int
    class TargetRoas(proto.Message):
        target_roas: float
    class TargetSpend(proto.Message):
        target_spend_micros: int
        cpc_bid_ceiling_micros: int
    resource_name: str
    id: int
    name: str
    type_: bidding_strategy_type.BiddingStrategyTypeEnum.BiddingStrategyType
    owner_customer_id: int
    owner_descriptive_name: str
    maximize_conversion_value: MaximizeConversionValue
    maximize_conversions: MaximizeConversions
    target_cpa: TargetCpa
    target_impression_share: TargetImpressionShare
    target_roas: TargetRoas
    target_spend: TargetSpend
