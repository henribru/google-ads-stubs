import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import account_link as gagr_account_link
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2

__protobuf__: Incomplete

class CreateAccountLinkRequest(proto.Message):
    customer_id: str
    account_link: gagr_account_link.AccountLink

class CreateAccountLinkResponse(proto.Message):
    resource_name: str

class MutateAccountLinkRequest(proto.Message):
    customer_id: str
    operation: AccountLinkOperation
    partial_failure: bool
    validate_only: bool

class AccountLinkOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    update: gagr_account_link.AccountLink
    remove: str

class MutateAccountLinkResponse(proto.Message):
    result: MutateAccountLinkResult
    partial_failure_error: status_pb2.Status

class MutateAccountLinkResult(proto.Message):
    resource_name: str
