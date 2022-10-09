import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class CreateAccountLinkRequest(proto.Message):
    customer_id: Incomplete
    account_link: Incomplete

class CreateAccountLinkResponse(proto.Message):
    resource_name: Incomplete

class MutateAccountLinkRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class AccountLinkOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAccountLinkResponse(proto.Message):
    result: Incomplete
    partial_failure_error: Incomplete

class MutateAccountLinkResult(proto.Message):
    resource_name: Incomplete
