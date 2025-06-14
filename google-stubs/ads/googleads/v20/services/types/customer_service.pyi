import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import access_role as gage_access_role, response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import customer as gagr_customer
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerRequest(proto.Message):
    customer_id: str
    operation: CustomerOperation
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CreateCustomerClientRequest(proto.Message):
    customer_id: str
    customer_client: gagr_customer.Customer
    email_address: str
    access_role: gage_access_role.AccessRoleEnum.AccessRole
    validate_only: bool

class CustomerOperation(proto.Message):
    update: gagr_customer.Customer
    update_mask: field_mask_pb2.FieldMask

class CreateCustomerClientResponse(proto.Message):
    resource_name: str
    invitation_link: str

class MutateCustomerResponse(proto.Message):
    result: MutateCustomerResult

class MutateCustomerResult(proto.Message):
    resource_name: str
    customer: gagr_customer.Customer

class ListAccessibleCustomersRequest(proto.Message): ...

class ListAccessibleCustomersResponse(proto.Message):
    resource_names: MutableSequence[str]
