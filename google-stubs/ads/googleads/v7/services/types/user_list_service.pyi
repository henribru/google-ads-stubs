from typing import Any

import proto

from google.ads.googleads.v7.resources.types import user_list as user_list

__protobuf__: Any

class GetUserListRequest(proto.Message):
    resource_name: Any

class MutateUserListsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class UserListOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateUserListsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateUserListResult(proto.Message):
    resource_name: Any
