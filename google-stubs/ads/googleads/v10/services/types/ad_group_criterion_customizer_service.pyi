from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.ad_group_criterion_customizer import (
    AdGroupCriterionCustomizer,
)

class AdGroupCriterionCustomizerOperation(proto.Message):
    create: AdGroupCriterionCustomizer
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AdGroupCriterionCustomizer = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupCriterionCustomizerResult(proto.Message):
    resource_name: str
    ad_group_criterion_customizer: AdGroupCriterionCustomizer
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_criterion_customizer: AdGroupCriterionCustomizer = ...
    ) -> None: ...

class MutateAdGroupCriterionCustomizersRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupCriterionCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupCriterionCustomizerOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupCriterionCustomizersResponse(proto.Message):
    results: list[MutateAdGroupCriterionCustomizerResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAdGroupCriterionCustomizerResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
