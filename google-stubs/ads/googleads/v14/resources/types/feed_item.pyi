from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v14.common.types.feed_common import Money
from google.ads.googleads.v14.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v14.enums.types.feed_item_quality_approval_status import (
    FeedItemQualityApprovalStatusEnum,
)
from google.ads.googleads.v14.enums.types.feed_item_quality_disapproval_reason import (
    FeedItemQualityDisapprovalReasonEnum,
)
from google.ads.googleads.v14.enums.types.feed_item_status import FeedItemStatusEnum
from google.ads.googleads.v14.enums.types.feed_item_validation_status import (
    FeedItemValidationStatusEnum,
)
from google.ads.googleads.v14.enums.types.geo_targeting_restriction import (
    GeoTargetingRestrictionEnum,
)
from google.ads.googleads.v14.enums.types.placeholder_type import PlaceholderTypeEnum
from google.ads.googleads.v14.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v14.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)
from google.ads.googleads.v14.errors.types.feed_item_validation_error import (
    FeedItemValidationErrorEnum,
)

_M = TypeVar("_M")

class FeedItem(proto.Message):
    resource_name: str
    feed: str
    id: int
    start_date_time: str
    end_date_time: str
    attribute_values: MutableSequence[FeedItemAttributeValue]
    geo_targeting_restriction: GeoTargetingRestrictionEnum.GeoTargetingRestriction
    url_custom_parameters: MutableSequence[CustomParameter]
    status: FeedItemStatusEnum.FeedItemStatus
    policy_infos: MutableSequence[FeedItemPlaceholderPolicyInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed: str = ...,
        id: int = ...,
        start_date_time: str = ...,
        end_date_time: str = ...,
        attribute_values: MutableSequence[FeedItemAttributeValue] = ...,
        geo_targeting_restriction: GeoTargetingRestrictionEnum.GeoTargetingRestriction = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
        status: FeedItemStatusEnum.FeedItemStatus = ...,
        policy_infos: MutableSequence[FeedItemPlaceholderPolicyInfo] = ...
    ) -> None: ...

class FeedItemAttributeValue(proto.Message):
    feed_attribute_id: int
    integer_value: int
    boolean_value: bool
    string_value: str
    double_value: float
    price_value: Money
    integer_values: MutableSequence[int]
    boolean_values: MutableSequence[bool]
    string_values: MutableSequence[str]
    double_values: MutableSequence[float]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        feed_attribute_id: int = ...,
        integer_value: int = ...,
        boolean_value: bool = ...,
        string_value: str = ...,
        double_value: float = ...,
        price_value: Money = ...,
        integer_values: MutableSequence[int] = ...,
        boolean_values: MutableSequence[bool] = ...,
        string_values: MutableSequence[str] = ...,
        double_values: MutableSequence[float] = ...
    ) -> None: ...

class FeedItemPlaceholderPolicyInfo(proto.Message):
    placeholder_type_enum: PlaceholderTypeEnum.PlaceholderType
    feed_mapping_resource_name: str
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    validation_status: FeedItemValidationStatusEnum.FeedItemValidationStatus
    validation_errors: MutableSequence[FeedItemValidationError]
    quality_approval_status: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    quality_disapproval_reasons: MutableSequence[
        FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        placeholder_type_enum: PlaceholderTypeEnum.PlaceholderType = ...,
        feed_mapping_resource_name: str = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...,
        policy_topic_entries: MutableSequence[PolicyTopicEntry] = ...,
        validation_status: FeedItemValidationStatusEnum.FeedItemValidationStatus = ...,
        validation_errors: MutableSequence[FeedItemValidationError] = ...,
        quality_approval_status: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus = ...,
        quality_disapproval_reasons: MutableSequence[
            FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
        ] = ...
    ) -> None: ...

class FeedItemValidationError(proto.Message):
    validation_error: FeedItemValidationErrorEnum.FeedItemValidationError
    description: str
    feed_attribute_ids: MutableSequence[int]
    extra_info: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        validation_error: FeedItemValidationErrorEnum.FeedItemValidationError = ...,
        description: str = ...,
        feed_attribute_ids: MutableSequence[int] = ...,
        extra_info: str = ...
    ) -> None: ...
