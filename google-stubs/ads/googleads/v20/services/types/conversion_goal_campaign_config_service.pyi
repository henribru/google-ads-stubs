import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import conversion_goal_campaign_config as gagr_conversion_goal_campaign_config
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateConversionGoalCampaignConfigsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ConversionGoalCampaignConfigOperation']
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class ConversionGoalCampaignConfigOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    update: gagr_conversion_goal_campaign_config.ConversionGoalCampaignConfig

class MutateConversionGoalCampaignConfigsResponse(proto.Message):
    results: MutableSequence['MutateConversionGoalCampaignConfigResult']

class MutateConversionGoalCampaignConfigResult(proto.Message):
    resource_name: str
    conversion_goal_campaign_config: gagr_conversion_goal_campaign_config.ConversionGoalCampaignConfig
