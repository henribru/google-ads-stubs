import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import custom_conversion_goal as gagr_custom_conversion_goal
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomConversionGoalOperation']
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CustomConversionGoalOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_custom_conversion_goal.CustomConversionGoal
    update: gagr_custom_conversion_goal.CustomConversionGoal
    remove: str

class MutateCustomConversionGoalsResponse(proto.Message):
    results: MutableSequence['MutateCustomConversionGoalResult']

class MutateCustomConversionGoalResult(proto.Message):
    resource_name: str
    custom_conversion_goal: gagr_custom_conversion_goal.CustomConversionGoal
