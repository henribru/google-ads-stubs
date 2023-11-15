from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.recommendation_subscription_status import (
    RecommendationSubscriptionStatusEnum,
)
from google.ads.googleads.v15.enums.types.recommendation_type import (
    RecommendationTypeEnum,
)

_M = TypeVar("_M")

class RecommendationSubscription(proto.Message):
    resource_name: str
    type_: RecommendationTypeEnum.RecommendationType
    create_date_time: str
    modify_date_time: str
    status: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        type_: RecommendationTypeEnum.RecommendationType = ...,
        create_date_time: str = ...,
        modify_date_time: str = ...,
        status: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus = ...
    ) -> None: ...
