from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v10.resources.types.customer_user_access import (
    CustomerUserAccess,
)

class CustomerUserAccessOperation(proto.Message):
    update_mask: FieldMask
    update: CustomerUserAccess
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: CustomerUserAccess = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerUserAccessRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessOperation
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: CustomerUserAccessOperation = ...
    ) -> None: ...

class MutateCustomerUserAccessResponse(proto.Message):
    result: MutateCustomerUserAccessResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateCustomerUserAccessResult = ...
    ) -> None: ...

class MutateCustomerUserAccessResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
