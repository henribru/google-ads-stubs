from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.customer_label import CustomerLabel

class CustomerLabelOperation(proto.Message):
    create: CustomerLabel
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CustomerLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCustomerLabelsRequest(proto.Message):
    customer_id: str
    operations: list[CustomerLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCustomerLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCustomerLabelResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCustomerLabelResult] = ...
    ) -> None: ...
