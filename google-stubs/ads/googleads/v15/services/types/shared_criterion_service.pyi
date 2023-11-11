from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.shared_criterion import SharedCriterion

_M = TypeVar("_M")

class MutateSharedCriteriaRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[SharedCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[SharedCriterionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateSharedCriteriaResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateSharedCriterionResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateSharedCriterionResult] = ...
    ) -> None: ...

class MutateSharedCriterionResult(proto.Message):
    resource_name: str
    shared_criterion: SharedCriterion
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        shared_criterion: SharedCriterion = ...
    ) -> None: ...

class SharedCriterionOperation(proto.Message):
    create: SharedCriterion
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: SharedCriterion = ...,
        remove: str = ...
    ) -> None: ...
