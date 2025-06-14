import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import goal_config_level as gage_goal_config_level

__protobuf__: Incomplete

class ConversionGoalCampaignConfig(proto.Message):
    resource_name: str
    campaign: str
    goal_config_level: gage_goal_config_level.GoalConfigLevelEnum.GoalConfigLevel
    custom_conversion_goal: str
