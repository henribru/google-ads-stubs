from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.ad_group_criterion_customizer import (
    AdGroupCriterionCustomizer,
)

_M = TypeVar("_M")

class AdGroupCriterionCustomizerOperation(proto.Message):
    create: AdGroupCriterionCustomizer
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: AdGroupCriterionCustomizer = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupCriterionCustomizerResult(proto.Message):
    resource_name: str
    ad_group_criterion_customizer: AdGroupCriterionCustomizer
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_criterion_customizer: AdGroupCriterionCustomizer = ...
    ) -> None: ...

class MutateAdGroupCriterionCustomizersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupCriterionCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupCriterionCustomizerOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupCriterionCustomizersResponse(proto.Message):
    results: MutableSequence[MutateAdGroupCriterionCustomizerResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAdGroupCriterionCustomizerResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
