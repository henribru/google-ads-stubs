from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

__protobuf__: Any

class MutateCustomConversionGoalsRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any
    response_content_type: Any

class CustomConversionGoalOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCustomConversionGoalsResponse(proto.Message):
    results: Any

class MutateCustomConversionGoalResult(proto.Message):
    resource_name: Any
    custom_conversion_goal: Any
