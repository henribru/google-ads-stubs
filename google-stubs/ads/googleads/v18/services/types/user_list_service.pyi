import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import user_list
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateUserListsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['UserListOperation']
    partial_failure: bool
    validate_only: bool

class UserListOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: user_list.UserList
    update: user_list.UserList
    remove: str

class MutateUserListsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateUserListResult']

class MutateUserListResult(proto.Message):
    resource_name: str
