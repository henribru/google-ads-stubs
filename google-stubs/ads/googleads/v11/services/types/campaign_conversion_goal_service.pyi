import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v11.resources.types import (
    campaign_conversion_goal as campaign_conversion_goal,
)

__protobuf__: Incomplete

class MutateCampaignConversionGoalsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete

class CampaignConversionGoalOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete

class MutateCampaignConversionGoalsResponse(proto.Message):
    results: Incomplete

class MutateCampaignConversionGoalResult(proto.Message):
    resource_name: Incomplete
