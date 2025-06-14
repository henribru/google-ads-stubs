from google.rpc.status_pb2 import Status
from google.ads.googleads.v19.resources.types.account_link import AccountLink
from google.ads.googleads.v19.resources.types.account_link import AccountLink
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AccountLinkOperation(proto.Message):
    update_mask: FieldMask
    update: AccountLink
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., update: AccountLink = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "update", "remove"]) -> bool: ...
class CreateAccountLinkRequest(proto.Message):
    customer_id: str
    account_link: AccountLink
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., account_link: AccountLink = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "account_link"]) -> bool: ...
class CreateAccountLinkResponse(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class MutateAccountLinkRequest(proto.Message):
    customer_id: str
    operation: AccountLinkOperation
    partial_failure: bool
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operation: AccountLinkOperation = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operation", "partial_failure", "validate_only"]) -> bool: ...
class MutateAccountLinkResponse(proto.Message):
    result: MutateAccountLinkResult
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, result: MutateAccountLinkResult = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["result", "partial_failure_error"]) -> bool: ...
class MutateAccountLinkResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
