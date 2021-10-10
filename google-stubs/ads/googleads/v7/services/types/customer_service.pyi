from typing import Any

import proto

__protobuf__: Any

class GetCustomerRequest(proto.Message):
    resource_name: Any

class MutateCustomerRequest(proto.Message):
    customer_id: Any
    operation: Any
    validate_only: Any
    response_content_type: Any

class CreateCustomerClientRequest(proto.Message):
    customer_id: Any
    customer_client: Any
    email_address: Any
    access_role: Any
    validate_only: Any

class CustomerOperation(proto.Message):
    update: Any
    update_mask: Any

class CreateCustomerClientResponse(proto.Message):
    resource_name: Any
    invitation_link: Any

class MutateCustomerResponse(proto.Message):
    result: Any

class MutateCustomerResult(proto.Message):
    resource_name: Any
    customer: Any

class ListAccessibleCustomersRequest(proto.Message): ...

class ListAccessibleCustomersResponse(proto.Message):
    resource_names: Any
