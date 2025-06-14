import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import user_list_customer_type
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateUserListCustomerTypesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['UserListCustomerTypeOperation']
    partial_failure: bool
    validate_only: bool

class UserListCustomerTypeOperation(proto.Message):
    create: user_list_customer_type.UserListCustomerType
    remove: str

class MutateUserListCustomerTypesResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateUserListCustomerTypeResult']

class MutateUserListCustomerTypeResult(proto.Message):
    resource_name: str
