from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v13.resources.types.customer_label import CustomerLabel

_M = TypeVar("_M")

class CustomerLabelOperation(proto.Message):
    create: CustomerLabel
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: CustomerLabel = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["create", "remove"]) -> bool: ...  # type: ignore[override]

class MutateCustomerLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class MutateCustomerLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CustomerLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only"]) -> bool: ...  # type: ignore[override]

class MutateCustomerLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCustomerLabelResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCustomerLabelResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]
