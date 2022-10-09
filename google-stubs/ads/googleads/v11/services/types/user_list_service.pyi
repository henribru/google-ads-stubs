import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.resources.types import user_list as user_list

__protobuf__: Incomplete

class MutateUserListsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class UserListOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateUserListsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateUserListResult(proto.Message):
    resource_name: Incomplete
