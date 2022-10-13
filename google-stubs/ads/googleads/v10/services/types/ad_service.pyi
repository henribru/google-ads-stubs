from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.common.types.policy import PolicyValidationParameter
from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.ad import Ad

class AdOperation(proto.Message):
    update_mask: FieldMask
    policy_validation_parameter: PolicyValidationParameter
    update: Ad
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        policy_validation_parameter: PolicyValidationParameter = ...,
        update: Ad = ...
    ) -> None: ...

class GetAdRequest(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAdResult(proto.Message):
    resource_name: str
    ad: Ad
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad: Ad = ...
    ) -> None: ...

class MutateAdsRequest(proto.Message):
    customer_id: str
    operations: list[AdOperation]
    partial_failure: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdOperation] = ...,
        partial_failure: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAdsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdResult] = ...
    ) -> None: ...
