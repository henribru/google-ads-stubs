from typing import Any

import proto

from google.ads.googleads.v15.enums.types.recommendation_subscription_status import (
    RecommendationSubscriptionStatusEnum,
)
from google.ads.googleads.v15.enums.types.recommendation_type import (
    RecommendationTypeEnum,
)

class RecommendationSubscription(proto.Message):
    resource_name: str
    type_: RecommendationTypeEnum.RecommendationType
    create_date_time: str
    modify_date_time: str
    status: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        type_: RecommendationTypeEnum.RecommendationType = ...,
        create_date_time: str = ...,
        modify_date_time: str = ...,
        status: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus = ...
    ) -> None: ...
