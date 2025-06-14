import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import recommendation_subscription as gagr_recommendation_subscription
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateRecommendationSubscriptionRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['RecommendationSubscriptionOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class RecommendationSubscriptionOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_recommendation_subscription.RecommendationSubscription
    update: gagr_recommendation_subscription.RecommendationSubscription

class MutateRecommendationSubscriptionResponse(proto.Message):
    results: MutableSequence['MutateRecommendationSubscriptionResult']
    partial_failure_error: status_pb2.Status

class MutateRecommendationSubscriptionResult(proto.Message):
    resource_name: str
    recommendation_subscription: gagr_recommendation_subscription.RecommendationSubscription
