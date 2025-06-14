import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import fixed_cpm_goal, fixed_cpm_target_frequency_time_unit, target_frequency_time_unit, target_impression_share_location

__protobuf__: Incomplete

class Commission(proto.Message):
    commission_rate_micros: int

class EnhancedCpc(proto.Message): ...
class ManualCpa(proto.Message): ...

class ManualCpc(proto.Message):
    enhanced_cpc_enabled: bool

class ManualCpm(proto.Message): ...
class ManualCpv(proto.Message): ...

class MaximizeConversions(proto.Message):
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    target_cpa_micros: int

class MaximizeConversionValue(proto.Message):
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int

class TargetCpa(proto.Message):
    target_cpa_micros: int
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int

class TargetCpm(proto.Message):
    target_frequency_goal: TargetCpmTargetFrequencyGoal

class TargetCpmTargetFrequencyGoal(proto.Message):
    target_count: int
    time_unit: target_frequency_time_unit.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit

class TargetImpressionShare(proto.Message):
    location: target_impression_share_location.TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    location_fraction_micros: int
    cpc_bid_ceiling_micros: int

class TargetRoas(proto.Message):
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int

class TargetSpend(proto.Message):
    target_spend_micros: int
    cpc_bid_ceiling_micros: int

class PercentCpc(proto.Message):
    cpc_bid_ceiling_micros: int
    enhanced_cpc_enabled: bool

class FixedCpm(proto.Message):
    goal: fixed_cpm_goal.FixedCpmGoalEnum.FixedCpmGoal
    target_frequency_info: FixedCpmTargetFrequencyGoalInfo

class FixedCpmTargetFrequencyGoalInfo(proto.Message):
    target_count: int
    time_unit: fixed_cpm_target_frequency_time_unit.FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit

class TargetCpv(proto.Message): ...
