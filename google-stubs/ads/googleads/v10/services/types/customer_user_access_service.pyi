import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v10.resources.types import (
    customer_user_access as customer_user_access,
)

__protobuf__: Incomplete

class MutateCustomerUserAccessRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete

class CustomerUserAccessOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateCustomerUserAccessResponse(proto.Message):
    result: Incomplete

class MutateCustomerUserAccessResult(proto.Message):
    resource_name: Incomplete
