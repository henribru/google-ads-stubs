from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.customer_negative_criterion import (
    CustomerNegativeCriterion,
)

_M = TypeVar("_M")

class CustomerNegativeCriterionOperation(proto.Message):
    create: CustomerNegativeCriterion
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: CustomerNegativeCriterion = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["create", "remove"]) -> bool: ...  # type: ignore[override]

class MutateCustomerNegativeCriteriaRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerNegativeCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CustomerNegativeCriterionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

class MutateCustomerNegativeCriteriaResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCustomerNegativeCriteriaResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCustomerNegativeCriteriaResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]

class MutateCustomerNegativeCriteriaResult(proto.Message):
    resource_name: str
    customer_negative_criterion: CustomerNegativeCriterion
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        customer_negative_criterion: CustomerNegativeCriterion = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "customer_negative_criterion"]) -> bool: ...  # type: ignore[override]
