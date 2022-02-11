from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetAccountLinkRequest(proto.Message):
    resource_name: Any

class CreateAccountLinkRequest(proto.Message):
    customer_id: Any
    account_link: Any

class CreateAccountLinkResponse(proto.Message):
    resource_name: Any

class MutateAccountLinkRequest(proto.Message):
    customer_id: Any
    operation: Any
    partial_failure: Any
    validate_only: Any

class AccountLinkOperation(proto.Message):
    update_mask: Any
    update: Any
    remove: Any

class MutateAccountLinkResponse(proto.Message):
    result: Any
    partial_failure_error: Any

class MutateAccountLinkResult(proto.Message):
    resource_name: Any
