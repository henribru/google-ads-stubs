from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.common.types.policy import PolicyValidationParameter
from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.ad_group_ad import AdGroupAd

class AdGroupAdOperation(proto.Message):
    update_mask: FieldMask
    policy_validation_parameter: PolicyValidationParameter
    create: AdGroupAd
    update: AdGroupAd
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        policy_validation_parameter: PolicyValidationParameter = ...,
        create: AdGroupAd = ...,
        update: AdGroupAd = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupAdResult(proto.Message):
    resource_name: str
    ad_group_ad: AdGroupAd
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_ad: AdGroupAd = ...
    ) -> None: ...

class MutateAdGroupAdsRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupAdOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupAdOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupAdsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdGroupAdResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdGroupAdResult] = ...
    ) -> None: ...
