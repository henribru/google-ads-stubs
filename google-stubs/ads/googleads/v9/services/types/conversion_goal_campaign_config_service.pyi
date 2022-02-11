from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

__protobuf__: Any

class MutateConversionGoalCampaignConfigsRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any
    response_content_type: Any

class ConversionGoalCampaignConfigOperation(proto.Message):
    update_mask: Any
    update: Any

class MutateConversionGoalCampaignConfigsResponse(proto.Message):
    results: Any

class MutateConversionGoalCampaignConfigResult(proto.Message):
    resource_name: Any
    conversion_goal_campaign_config: Any
