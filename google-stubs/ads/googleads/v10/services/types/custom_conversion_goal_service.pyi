import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

__protobuf__: Incomplete

class MutateCustomConversionGoalsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CustomConversionGoalOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateCustomConversionGoalsResponse(proto.Message):
    results: Incomplete

class MutateCustomConversionGoalResult(proto.Message):
    resource_name: Incomplete
    custom_conversion_goal: Incomplete
