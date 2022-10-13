from typing import Any

import proto

from google.ads.googleads.v10.resources.types.customer_user_access_invitation import (
    CustomerUserAccessInvitation,
)

class CustomerUserAccessInvitationOperation(proto.Message):
    create: CustomerUserAccessInvitation
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CustomerUserAccessInvitation = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerUserAccessInvitationRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessInvitationOperation
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: CustomerUserAccessInvitationOperation = ...
    ) -> None: ...

class MutateCustomerUserAccessInvitationResponse(proto.Message):
    result: MutateCustomerUserAccessInvitationResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateCustomerUserAccessInvitationResult = ...
    ) -> None: ...

class MutateCustomerUserAccessInvitationResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
