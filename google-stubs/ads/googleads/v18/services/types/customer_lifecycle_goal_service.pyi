import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import customer_lifecycle_goal
from google.protobuf import field_mask_pb2

__protobuf__: Incomplete

class ConfigureCustomerLifecycleGoalsRequest(proto.Message):
    customer_id: str
    operation: CustomerLifecycleGoalOperation
    validate_only: bool

class CustomerLifecycleGoalOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: customer_lifecycle_goal.CustomerLifecycleGoal
    update: customer_lifecycle_goal.CustomerLifecycleGoal

class ConfigureCustomerLifecycleGoalsResponse(proto.Message):
    result: ConfigureCustomerLifecycleGoalsResult

class ConfigureCustomerLifecycleGoalsResult(proto.Message):
    resource_name: str
