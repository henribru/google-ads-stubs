import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import lifecycle_goals

__protobuf__: Incomplete

class CustomerLifecycleGoal(proto.Message):
    resource_name: str
    customer_acquisition_goal_value_settings: lifecycle_goals.LifecycleGoalValueSettings
    owner_customer: str
