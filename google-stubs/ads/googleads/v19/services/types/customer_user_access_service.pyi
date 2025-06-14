import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import customer_user_access
from google.protobuf import field_mask_pb2

__protobuf__: Incomplete

class MutateCustomerUserAccessRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessOperation

class CustomerUserAccessOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    update: customer_user_access.CustomerUserAccess
    remove: str

class MutateCustomerUserAccessResponse(proto.Message):
    result: MutateCustomerUserAccessResult

class MutateCustomerUserAccessResult(proto.Message):
    resource_name: str
