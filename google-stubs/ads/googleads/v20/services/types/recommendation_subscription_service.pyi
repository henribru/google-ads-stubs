from google.ads.googleads.v20.resources.types.recommendation_subscription import RecommendationSubscription
from google.ads.googleads.v20.resources.types.recommendation_subscription import RecommendationSubscription
from google.protobuf.field_mask_pb2 import FieldMask
from google.ads.googleads.v20.resources.types.recommendation_subscription import RecommendationSubscription
from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v20.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class MutateRecommendationSubscriptionRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[RecommendationSubscriptionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[RecommendationSubscriptionOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateRecommendationSubscriptionResponse(proto.Message):
    results: MutableSequence[MutateRecommendationSubscriptionResult]
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, results: MutableSequence[MutateRecommendationSubscriptionResult] = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results", "partial_failure_error"]) -> bool: ...
class MutateRecommendationSubscriptionResult(proto.Message):
    resource_name: str
    recommendation_subscription: RecommendationSubscription
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., recommendation_subscription: RecommendationSubscription = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "recommendation_subscription"]) -> bool: ...
class RecommendationSubscriptionOperation(proto.Message):
    update_mask: FieldMask
    create: RecommendationSubscription
    update: RecommendationSubscription
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: RecommendationSubscription = ..., update: RecommendationSubscription = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update"]) -> bool: ...
