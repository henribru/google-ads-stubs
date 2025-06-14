import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import campaign_conversion_goal
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignConversionGoalOperation']
    validate_only: bool

class CampaignConversionGoalOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    update: campaign_conversion_goal.CampaignConversionGoal

class MutateCampaignConversionGoalsResponse(proto.Message):
    results: MutableSequence['MutateCampaignConversionGoalResult']

class MutateCampaignConversionGoalResult(proto.Message):
    resource_name: str
