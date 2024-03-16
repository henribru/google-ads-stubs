from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.resources.types.customer_user_access_invitation import (
    CustomerUserAccessInvitation,
)

_M = TypeVar("_M")

class CustomerUserAccessInvitationOperation(proto.Message):
    create: CustomerUserAccessInvitation
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: CustomerUserAccessInvitation = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["create", "remove"]
    ) -> bool: ...

class MutateCustomerUserAccessInvitationRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessInvitationOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: CustomerUserAccessInvitationOperation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operation"]
    ) -> bool: ...

class MutateCustomerUserAccessInvitationResponse(proto.Message):
    result: MutateCustomerUserAccessInvitationResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateCustomerUserAccessInvitationResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result"]
    ) -> bool: ...

class MutateCustomerUserAccessInvitationResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name"]
    ) -> bool: ...
