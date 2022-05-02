import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v10.resources.types import (
    customer_conversion_goal as customer_conversion_goal,
)

__protobuf__: Incomplete

class MutateCustomerConversionGoalsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete

class CustomerConversionGoalOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete

class MutateCustomerConversionGoalsResponse(proto.Message):
    results: Incomplete

class MutateCustomerConversionGoalResult(proto.Message):
    resource_name: Incomplete
