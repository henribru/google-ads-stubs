from google.ads.googleads.v18.enums.types.recommendation_subscription_status import RecommendationSubscriptionStatusEnum
from google.ads.googleads.v18.enums.types.recommendation_type import RecommendationTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class RecommendationSubscription(proto.Message):
    resource_name: str
    type_: RecommendationTypeEnum.RecommendationType
    create_date_time: str
    modify_date_time: str
    status: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., type_: RecommendationTypeEnum.RecommendationType = ..., create_date_time: str = ..., modify_date_time: str = ..., status: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "type_", "create_date_time", "modify_date_time", "status"]) -> bool: ...
