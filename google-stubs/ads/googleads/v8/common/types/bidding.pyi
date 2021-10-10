from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    target_impression_share_location as target_impression_share_location,
)

__protobuf__: Any

class Commission(proto.Message):
    commission_rate_micros: Any

class EnhancedCpc(proto.Message): ...

class ManualCpc(proto.Message):
    enhanced_cpc_enabled: Any

class ManualCpm(proto.Message): ...
class ManualCpv(proto.Message): ...

class MaximizeConversions(proto.Message):
    target_cpa: Any

class MaximizeConversionValue(proto.Message):
    target_roas: Any

class TargetCpa(proto.Message):
    target_cpa_micros: Any
    cpc_bid_ceiling_micros: Any
    cpc_bid_floor_micros: Any

class TargetCpm(proto.Message): ...

class TargetImpressionShare(proto.Message):
    location: Any
    location_fraction_micros: Any
    cpc_bid_ceiling_micros: Any

class TargetRoas(proto.Message):
    target_roas: Any
    cpc_bid_ceiling_micros: Any
    cpc_bid_floor_micros: Any

class TargetSpend(proto.Message):
    target_spend_micros: Any
    cpc_bid_ceiling_micros: Any

class PercentCpc(proto.Message):
    cpc_bid_ceiling_micros: Any
    enhanced_cpc_enabled: Any
