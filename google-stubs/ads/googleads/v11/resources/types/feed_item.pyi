from typing import Any

import proto

from google.ads.googleads.v11.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v11.common.types.feed_common import Money
from google.ads.googleads.v11.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v11.enums.types.feed_item_quality_approval_status import (
    FeedItemQualityApprovalStatusEnum,
)
from google.ads.googleads.v11.enums.types.feed_item_quality_disapproval_reason import (
    FeedItemQualityDisapprovalReasonEnum,
)
from google.ads.googleads.v11.enums.types.feed_item_status import FeedItemStatusEnum
from google.ads.googleads.v11.enums.types.feed_item_validation_status import (
    FeedItemValidationStatusEnum,
)
from google.ads.googleads.v11.enums.types.geo_targeting_restriction import (
    GeoTargetingRestrictionEnum,
)
from google.ads.googleads.v11.enums.types.placeholder_type import PlaceholderTypeEnum
from google.ads.googleads.v11.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v11.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)
from google.ads.googleads.v11.errors.types.feed_item_validation_error import (
    FeedItemValidationErrorEnum,
)

class FeedItem(proto.Message):
    resource_name: str
    feed: str
    id: int
    start_date_time: str
    end_date_time: str
    attribute_values: list[FeedItemAttributeValue]
    geo_targeting_restriction: GeoTargetingRestrictionEnum.GeoTargetingRestriction
    url_custom_parameters: list[CustomParameter]
    status: FeedItemStatusEnum.FeedItemStatus
    policy_infos: list[FeedItemPlaceholderPolicyInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed: str = ...,
        id: int = ...,
        start_date_time: str = ...,
        end_date_time: str = ...,
        attribute_values: list[FeedItemAttributeValue] = ...,
        geo_targeting_restriction: GeoTargetingRestrictionEnum.GeoTargetingRestriction = ...,
        url_custom_parameters: list[CustomParameter] = ...,
        status: FeedItemStatusEnum.FeedItemStatus = ...,
        policy_infos: list[FeedItemPlaceholderPolicyInfo] = ...
    ) -> None: ...

class FeedItemAttributeValue(proto.Message):
    feed_attribute_id: int
    integer_value: int
    boolean_value: bool
    string_value: str
    double_value: float
    price_value: Money
    integer_values: list[int]
    boolean_values: list[bool]
    string_values: list[str]
    double_values: list[float]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        feed_attribute_id: int = ...,
        integer_value: int = ...,
        boolean_value: bool = ...,
        string_value: str = ...,
        double_value: float = ...,
        price_value: Money = ...,
        integer_values: list[int] = ...,
        boolean_values: list[bool] = ...,
        string_values: list[str] = ...,
        double_values: list[float] = ...
    ) -> None: ...

class FeedItemPlaceholderPolicyInfo(proto.Message):
    placeholder_type_enum: PlaceholderTypeEnum.PlaceholderType
    feed_mapping_resource_name: str
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    policy_topic_entries: list[PolicyTopicEntry]
    validation_status: FeedItemValidationStatusEnum.FeedItemValidationStatus
    validation_errors: list[FeedItemValidationError]
    quality_approval_status: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    quality_disapproval_reasons: list[
        FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    ]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        placeholder_type_enum: PlaceholderTypeEnum.PlaceholderType = ...,
        feed_mapping_resource_name: str = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...,
        policy_topic_entries: list[PolicyTopicEntry] = ...,
        validation_status: FeedItemValidationStatusEnum.FeedItemValidationStatus = ...,
        validation_errors: list[FeedItemValidationError] = ...,
        quality_approval_status: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus = ...,
        quality_disapproval_reasons: list[
            FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
        ] = ...
    ) -> None: ...

class FeedItemValidationError(proto.Message):
    validation_error: FeedItemValidationErrorEnum.FeedItemValidationError
    description: str
    feed_attribute_ids: list[int]
    extra_info: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        validation_error: FeedItemValidationErrorEnum.FeedItemValidationError = ...,
        description: str = ...,
        feed_attribute_ids: list[int] = ...,
        extra_info: str = ...
    ) -> None: ...
