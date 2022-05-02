import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

__protobuf__: Incomplete

class MutateConversionGoalCampaignConfigsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class ConversionGoalCampaignConfigOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete

class MutateConversionGoalCampaignConfigsResponse(proto.Message):
    results: Incomplete

class MutateConversionGoalCampaignConfigResult(proto.Message):
    resource_name: Incomplete
    conversion_goal_campaign_config: Incomplete
