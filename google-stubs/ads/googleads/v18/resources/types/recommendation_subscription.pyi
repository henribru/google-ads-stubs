import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import recommendation_subscription_status, recommendation_type

__protobuf__: Incomplete

class RecommendationSubscription(proto.Message):
    resource_name: str
    type_: recommendation_type.RecommendationTypeEnum.RecommendationType
    create_date_time: str
    modify_date_time: str
    status: recommendation_subscription_status.RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
