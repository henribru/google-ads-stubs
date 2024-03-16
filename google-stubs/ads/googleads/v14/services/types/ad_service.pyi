from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.policy import PolicyValidationParameter
from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.ad import Ad

_M = TypeVar("_M")

class AdOperation(proto.Message):
    update_mask: FieldMask
    policy_validation_parameter: PolicyValidationParameter
    update: Ad
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        policy_validation_parameter: PolicyValidationParameter = ...,
        update: Ad = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "policy_validation_parameter", "update"]
    ) -> bool: ...

class GetAdRequest(proto.Message):
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

class MutateAdResult(proto.Message):
    resource_name: str
    ad: Ad
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad: Ad = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "ad"]
    ) -> bool: ...

class MutateAdsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdOperation]
    partial_failure: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdOperation] = ...,
        partial_failure: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "operations",
            "partial_failure",
            "response_content_type",
            "validate_only",
        ],
    ) -> bool: ...

class MutateAdsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "results"]
    ) -> bool: ...
