from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.ad_parameter import AdParameter

_M = TypeVar("_M")

class AdParameterOperation(proto.Message):
    update_mask: FieldMask
    create: AdParameter
    update: AdParameter
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AdParameter = ...,
        update: AdParameter = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...  # type: ignore[override]

class MutateAdParameterResult(proto.Message):
    resource_name: str
    ad_parameter: AdParameter
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_parameter: AdParameter = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "ad_parameter"]) -> bool: ...  # type: ignore[override]

class MutateAdParametersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdParameterOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdParameterOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

class MutateAdParametersResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdParameterResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdParameterResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]
