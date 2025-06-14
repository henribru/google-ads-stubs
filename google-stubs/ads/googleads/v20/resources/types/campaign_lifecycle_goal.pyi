import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import lifecycle_goals
from google.ads.googleads.v20.enums.types import customer_acquisition_optimization_mode

__protobuf__: Incomplete

class CampaignLifecycleGoal(proto.Message):
    resource_name: str
    campaign: str
    customer_acquisition_goal_settings: CustomerAcquisitionGoalSettings

class CustomerAcquisitionGoalSettings(proto.Message):
    optimization_mode: customer_acquisition_optimization_mode.CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    value_settings: lifecycle_goals.LifecycleGoalValueSettings
