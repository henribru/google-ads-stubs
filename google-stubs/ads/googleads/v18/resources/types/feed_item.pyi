from collections.abc import MutableSequence
from google.ads.googleads.v18.errors.types.feed_item_validation_error import FeedItemValidationErrorEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.feed_item_quality_disapproval_reason import FeedItemQualityDisapprovalReasonEnum
from google.ads.googleads.v18.enums.types.feed_item_quality_approval_status import FeedItemQualityApprovalStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.feed_item_validation_status import FeedItemValidationStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v18.enums.types.policy_approval_status import PolicyApprovalStatusEnum
from google.ads.googleads.v18.enums.types.policy_review_status import PolicyReviewStatusEnum
from google.ads.googleads.v18.enums.types.placeholder_type import PlaceholderTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.feed_common import Money
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.feed_item_status import FeedItemStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v18.enums.types.geo_targeting_restriction import GeoTargetingRestrictionEnum
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., feed: str = ..., id: int = ..., start_date_time: str = ..., end_date_time: str = ..., attribute_values: MutableSequence[FeedItemAttributeValue] = ..., geo_targeting_restriction: GeoTargetingRestrictionEnum.GeoTargetingRestriction = ..., url_custom_parameters: MutableSequence[CustomParameter] = ..., status: FeedItemStatusEnum.FeedItemStatus = ..., policy_infos: MutableSequence[FeedItemPlaceholderPolicyInfo] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "feed", "id", "start_date_time", "end_date_time", "attribute_values", "geo_targeting_restriction", "url_custom_parameters", "status", "policy_infos"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., feed_attribute_id: int = ..., integer_value: int = ..., boolean_value: bool = ..., string_value: str = ..., double_value: float = ..., price_value: Money = ..., integer_values: MutableSequence[int] = ..., boolean_values: MutableSequence[bool] = ..., string_values: MutableSequence[str] = ..., double_values: MutableSequence[float] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["feed_attribute_id", "integer_value", "boolean_value", "string_value", "double_value", "price_value", "integer_values", "boolean_values", "string_values", "double_values"]) -> bool: ...
class FeedItemPlaceholderPolicyInfo(proto.Message):
    placeholder_type_enum: PlaceholderTypeEnum.PlaceholderType
    feed_mapping_resource_name: str
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    validation_status: FeedItemValidationStatusEnum.FeedItemValidationStatus
    validation_errors: MutableSequence[FeedItemValidationError]
    quality_approval_status: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    quality_disapproval_reasons: MutableSequence[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., placeholder_type_enum: PlaceholderTypeEnum.PlaceholderType = ..., feed_mapping_resource_name: str = ..., review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ..., approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ..., policy_topic_entries: MutableSequence[PolicyTopicEntry] = ..., validation_status: FeedItemValidationStatusEnum.FeedItemValidationStatus = ..., validation_errors: MutableSequence[FeedItemValidationError] = ..., quality_approval_status: FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus = ..., quality_disapproval_reasons: MutableSequence[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["placeholder_type_enum", "feed_mapping_resource_name", "review_status", "approval_status", "policy_topic_entries", "validation_status", "validation_errors", "quality_approval_status", "quality_disapproval_reasons"]) -> bool: ...
class FeedItemValidationError(proto.Message):
    validation_error: FeedItemValidationErrorEnum.FeedItemValidationError
    description: str
    feed_attribute_ids: MutableSequence[int]
    extra_info: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., validation_error: FeedItemValidationErrorEnum.FeedItemValidationError = ..., description: str = ..., feed_attribute_ids: MutableSequence[int] = ..., extra_info: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["validation_error", "description", "feed_attribute_ids", "extra_info"]) -> bool: ...
