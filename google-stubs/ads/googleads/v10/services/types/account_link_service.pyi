from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.account_link import AccountLink

class AccountLinkOperation(proto.Message):
    update_mask: FieldMask
    update: AccountLink
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: AccountLink = ...,
        remove: str = ...
    ) -> None: ...

class CreateAccountLinkRequest(proto.Message):
    customer_id: str
    account_link: AccountLink
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        account_link: AccountLink = ...
    ) -> None: ...

class CreateAccountLinkResponse(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAccountLinkRequest(proto.Message):
    customer_id: str
    operation: AccountLinkOperation
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: AccountLinkOperation = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAccountLinkResponse(proto.Message):
    result: MutateAccountLinkResult
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateAccountLinkResult = ...,
        partial_failure_error: Status = ...
    ) -> None: ...

class MutateAccountLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
