import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import campaign_lifecycle_goal
from google.protobuf import field_mask_pb2

__protobuf__: Incomplete

class ConfigureCampaignLifecycleGoalsRequest(proto.Message):
    customer_id: str
    operation: CampaignLifecycleGoalOperation
    validate_only: bool

class CampaignLifecycleGoalOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: campaign_lifecycle_goal.CampaignLifecycleGoal
    update: campaign_lifecycle_goal.CampaignLifecycleGoal

class ConfigureCampaignLifecycleGoalsResponse(proto.Message):
    result: ConfigureCampaignLifecycleGoalsResult

class ConfigureCampaignLifecycleGoalsResult(proto.Message):
    resource_name: str
