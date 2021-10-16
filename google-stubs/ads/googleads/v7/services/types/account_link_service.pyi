from typing import Any

import proto

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

class MutateAccountLinkResult(proto.Message):
    resource_name: Any
