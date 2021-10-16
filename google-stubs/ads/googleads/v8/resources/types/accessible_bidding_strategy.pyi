from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    bidding_strategy_type as bidding_strategy_type,
    target_impression_share_location as target_impression_share_location,
)

__protobuf__: Any

class AccessibleBiddingStrategy(proto.Message):
    class MaximizeConversionValue(proto.Message):
        target_roas: Any
    class MaximizeConversions(proto.Message):
        target_cpa: Any
    class TargetCpa(proto.Message):
        target_cpa_micros: Any
    class TargetSpend(proto.Message):
        target_spend_micros: Any
        cpc_bid_ceiling_micros: Any
    class TargetImpressionShare(proto.Message):
        location: Any
        location_fraction_micros: Any
        cpc_bid_ceiling_micros: Any
    class TargetRoas(proto.Message):
        target_roas: Any
    resource_name: Any
    id: Any
    name: Any
    type_: Any
    owner_customer_id: Any
    owner_descriptive_name: Any
    maximize_conversion_value: Any
    maximize_conversions: Any
    target_cpa: Any
    target_impression_share: Any
    target_roas: Any
    target_spend: Any
