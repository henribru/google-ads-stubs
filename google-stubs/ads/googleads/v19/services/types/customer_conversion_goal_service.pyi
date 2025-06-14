import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import customer_conversion_goal
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerConversionGoalOperation']
    validate_only: bool

class CustomerConversionGoalOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    update: customer_conversion_goal.CustomerConversionGoal

class MutateCustomerConversionGoalsResponse(proto.Message):
    results: MutableSequence['MutateCustomerConversionGoalResult']

class MutateCustomerConversionGoalResult(proto.Message):
    resource_name: str
