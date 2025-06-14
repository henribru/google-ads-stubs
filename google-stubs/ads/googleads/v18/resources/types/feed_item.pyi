import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import custom_parameter, feed_common, policy
from google.ads.googleads.v18.enums.types import feed_item_quality_approval_status, feed_item_quality_disapproval_reason, feed_item_status, feed_item_validation_status, geo_targeting_restriction as gage_geo_targeting_restriction, placeholder_type, policy_approval_status, policy_review_status
from google.ads.googleads.v18.errors.types import feed_item_validation_error
from typing import MutableSequence

__protobuf__: Incomplete

class FeedItem(proto.Message):
    resource_name: str
    feed: str
    id: int
    start_date_time: str
    end_date_time: str
    attribute_values: MutableSequence['FeedItemAttributeValue']
    geo_targeting_restriction: gage_geo_targeting_restriction.GeoTargetingRestrictionEnum.GeoTargetingRestriction
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
    status: feed_item_status.FeedItemStatusEnum.FeedItemStatus
    policy_infos: MutableSequence['FeedItemPlaceholderPolicyInfo']

class FeedItemAttributeValue(proto.Message):
    feed_attribute_id: int
    integer_value: int
    boolean_value: bool
    string_value: str
    double_value: float
    price_value: feed_common.Money
    integer_values: MutableSequence[int]
    boolean_values: MutableSequence[bool]
    string_values: MutableSequence[str]
    double_values: MutableSequence[float]

class FeedItemPlaceholderPolicyInfo(proto.Message):
    placeholder_type_enum: placeholder_type.PlaceholderTypeEnum.PlaceholderType
    feed_mapping_resource_name: str
    review_status: policy_review_status.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: policy_approval_status.PolicyApprovalStatusEnum.PolicyApprovalStatus
    policy_topic_entries: MutableSequence[policy.PolicyTopicEntry]
    validation_status: feed_item_validation_status.FeedItemValidationStatusEnum.FeedItemValidationStatus
    validation_errors: MutableSequence['FeedItemValidationError']
    quality_approval_status: feed_item_quality_approval_status.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    quality_disapproval_reasons: MutableSequence[feed_item_quality_disapproval_reason.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]

class FeedItemValidationError(proto.Message):
    validation_error: feed_item_validation_error.FeedItemValidationErrorEnum.FeedItemValidationError
    description: str
    feed_attribute_ids: MutableSequence[int]
    extra_info: str
