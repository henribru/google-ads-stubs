import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

__protobuf__: Incomplete

class MutateCustomerRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CreateCustomerClientRequest(proto.Message):
    customer_id: Incomplete
    customer_client: Incomplete
    email_address: Incomplete
    access_role: Incomplete
    validate_only: Incomplete

class CustomerOperation(proto.Message):
    update: Incomplete
    update_mask: Incomplete

class CreateCustomerClientResponse(proto.Message):
    resource_name: Incomplete
    invitation_link: Incomplete

class MutateCustomerResponse(proto.Message):
    result: Incomplete

class MutateCustomerResult(proto.Message):
    resource_name: Incomplete
    customer: Incomplete

class ListAccessibleCustomersRequest(proto.Message): ...

class ListAccessibleCustomersResponse(proto.Message):
    resource_names: Incomplete
