from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v9.resources.types import (
    campaign_conversion_goal as campaign_conversion_goal,
)

__protobuf__: Any

class MutateCampaignConversionGoalsRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any

class CampaignConversionGoalOperation(proto.Message):
    update_mask: Any
    update: Any

class MutateCampaignConversionGoalsResponse(proto.Message):
    results: Any

class MutateCampaignConversionGoalResult(proto.Message):
    resource_name: Any
