from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v9.resources.types import (
    customer_conversion_goal as customer_conversion_goal,
)

__protobuf__: Any

class MutateCustomerConversionGoalsRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any

class CustomerConversionGoalOperation(proto.Message):
    update_mask: Any
    update: Any

class MutateCustomerConversionGoalsResponse(proto.Message):
    results: Any

class MutateCustomerConversionGoalResult(proto.Message):
    resource_name: Any
