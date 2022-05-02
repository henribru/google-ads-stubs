import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    bidding_strategy_type as bidding_strategy_type,
    target_impression_share_location as target_impression_share_location,
)

__protobuf__: Incomplete

class AccessibleBiddingStrategy(proto.Message):
    class MaximizeConversionValue(proto.Message):
        target_roas: Incomplete

    class MaximizeConversions(proto.Message):
        target_cpa: Incomplete

    class TargetCpa(proto.Message):
        target_cpa_micros: Incomplete

    class TargetImpressionShare(proto.Message):
        location: Incomplete
        location_fraction_micros: Incomplete
        cpc_bid_ceiling_micros: Incomplete

    class TargetRoas(proto.Message):
        target_roas: Incomplete

    class TargetSpend(proto.Message):
        target_spend_micros: Incomplete
        cpc_bid_ceiling_micros: Incomplete
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    type_: Incomplete
    owner_customer_id: Incomplete
    owner_descriptive_name: Incomplete
    maximize_conversion_value: Incomplete
    maximize_conversions: Incomplete
    target_cpa: Incomplete
    target_impression_share: Incomplete
    target_roas: Incomplete
    target_spend: Incomplete
