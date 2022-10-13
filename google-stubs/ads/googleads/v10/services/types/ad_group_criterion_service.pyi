from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.common.types.policy import PolicyViolationKey
from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.ad_group_criterion import AdGroupCriterion

class AdGroupCriterionOperation(proto.Message):
    update_mask: FieldMask
    exempt_policy_violation_keys: list[PolicyViolationKey]
    create: AdGroupCriterion
    update: AdGroupCriterion
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        exempt_policy_violation_keys: list[PolicyViolationKey] = ...,
        create: AdGroupCriterion = ...,
        update: AdGroupCriterion = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupCriteriaRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupCriterionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupCriteriaResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdGroupCriterionResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdGroupCriterionResult] = ...
    ) -> None: ...

class MutateAdGroupCriterionResult(proto.Message):
    resource_name: str
    ad_group_criterion: AdGroupCriterion
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_criterion: AdGroupCriterion = ...
    ) -> None: ...
