import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    target_impression_share_location as target_impression_share_location,
)

__protobuf__: Incomplete

class Commission(proto.Message):
    commission_rate_micros: Incomplete

class EnhancedCpc(proto.Message): ...
class ManualCpa(proto.Message): ...

class ManualCpc(proto.Message):
    enhanced_cpc_enabled: Incomplete

class ManualCpm(proto.Message): ...
class ManualCpv(proto.Message): ...

class MaximizeConversions(proto.Message):
    cpc_bid_ceiling_micros: Incomplete
    cpc_bid_floor_micros: Incomplete
    target_cpa_micros: Incomplete

class MaximizeConversionValue(proto.Message):
    target_roas: Incomplete
    cpc_bid_ceiling_micros: Incomplete
    cpc_bid_floor_micros: Incomplete

class TargetCpa(proto.Message):
    target_cpa_micros: Incomplete
    cpc_bid_ceiling_micros: Incomplete
    cpc_bid_floor_micros: Incomplete

class TargetCpm(proto.Message): ...

class TargetImpressionShare(proto.Message):
    location: Incomplete
    location_fraction_micros: Incomplete
    cpc_bid_ceiling_micros: Incomplete

class TargetRoas(proto.Message):
    target_roas: Incomplete
    cpc_bid_ceiling_micros: Incomplete
    cpc_bid_floor_micros: Incomplete

class TargetSpend(proto.Message):
    target_spend_micros: Incomplete
    cpc_bid_ceiling_micros: Incomplete

class PercentCpc(proto.Message):
    cpc_bid_ceiling_micros: Incomplete
    enhanced_cpc_enabled: Incomplete
