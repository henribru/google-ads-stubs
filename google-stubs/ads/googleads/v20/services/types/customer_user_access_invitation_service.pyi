from google.ads.googleads.v20.resources.types.customer_user_access_invitation import CustomerUserAccessInvitation
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerUserAccessInvitationOperation(proto.Message):
    create: CustomerUserAccessInvitation
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., create: CustomerUserAccessInvitation = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
class MutateCustomerUserAccessInvitationRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessInvitationOperation
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operation: CustomerUserAccessInvitationOperation = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operation"]) -> bool: ...
class MutateCustomerUserAccessInvitationResponse(proto.Message):
    result: MutateCustomerUserAccessInvitationResult
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., result: MutateCustomerUserAccessInvitationResult = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["result"]) -> bool: ...
class MutateCustomerUserAccessInvitationResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
