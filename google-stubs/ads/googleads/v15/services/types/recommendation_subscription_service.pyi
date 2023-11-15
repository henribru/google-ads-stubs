from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.recommendation_subscription import (
    RecommendationSubscription,
)

_M = TypeVar("_M")

class MutateRecommendationSubscriptionRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[RecommendationSubscriptionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[RecommendationSubscriptionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateRecommendationSubscriptionResponse(proto.Message):
    results: MutableSequence[MutateRecommendationSubscriptionResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateRecommendationSubscriptionResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...

class MutateRecommendationSubscriptionResult(proto.Message):
    resource_name: str
    recommendation_subscription: RecommendationSubscription
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        recommendation_subscription: RecommendationSubscription = ...
    ) -> None: ...

class RecommendationSubscriptionOperation(proto.Message):
    update_mask: FieldMask
    create: RecommendationSubscription
    update: RecommendationSubscription
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: RecommendationSubscription = ...,
        update: RecommendationSubscription = ...
    ) -> None: ...
