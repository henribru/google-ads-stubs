import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    custom_parameter as custom_parameter,
    feed_common as feed_common,
    policy as policy,
)
from google.ads.googleads.v11.enums.types import (
    feed_item_quality_approval_status as feed_item_quality_approval_status,
    feed_item_quality_disapproval_reason as feed_item_quality_disapproval_reason,
    feed_item_status as feed_item_status,
    feed_item_validation_status as feed_item_validation_status,
    placeholder_type as placeholder_type,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)
from google.ads.googleads.v11.errors.types import (
    feed_item_validation_error as feed_item_validation_error,
)

__protobuf__: Incomplete

class FeedItem(proto.Message):
    resource_name: Incomplete
    feed: Incomplete
    id: Incomplete
    start_date_time: Incomplete
    end_date_time: Incomplete
    attribute_values: Incomplete
    geo_targeting_restriction: Incomplete
    url_custom_parameters: Incomplete
    status: Incomplete
    policy_infos: Incomplete

class FeedItemAttributeValue(proto.Message):
    feed_attribute_id: Incomplete
    integer_value: Incomplete
    boolean_value: Incomplete
    string_value: Incomplete
    double_value: Incomplete
    price_value: Incomplete
    integer_values: Incomplete
    boolean_values: Incomplete
    string_values: Incomplete
    double_values: Incomplete

class FeedItemPlaceholderPolicyInfo(proto.Message):
    placeholder_type_enum: Incomplete
    feed_mapping_resource_name: Incomplete
    review_status: Incomplete
    approval_status: Incomplete
    policy_topic_entries: Incomplete
    validation_status: Incomplete
    validation_errors: Incomplete
    quality_approval_status: Incomplete
    quality_disapproval_reasons: Incomplete

class FeedItemValidationError(proto.Message):
    validation_error: Incomplete
    description: Incomplete
    feed_attribute_ids: Incomplete
    extra_info: Incomplete
