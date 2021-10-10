from typing import Any

import proto

from google.ads.googleads.v8.common.types import (
    custom_parameter as custom_parameter,
    feed_common as feed_common,
    policy as policy,
)
from google.ads.googleads.v8.enums.types import (
    feed_item_quality_approval_status as feed_item_quality_approval_status,
    feed_item_quality_disapproval_reason as feed_item_quality_disapproval_reason,
    feed_item_status as feed_item_status,
    feed_item_validation_status as feed_item_validation_status,
    placeholder_type as placeholder_type,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)
from google.ads.googleads.v8.errors.types import (
    feed_item_validation_error as feed_item_validation_error,
)

__protobuf__: Any

class FeedItem(proto.Message):
    resource_name: Any
    feed: Any
    id: Any
    start_date_time: Any
    end_date_time: Any
    attribute_values: Any
    geo_targeting_restriction: Any
    url_custom_parameters: Any
    status: Any
    policy_infos: Any

class FeedItemAttributeValue(proto.Message):
    feed_attribute_id: Any
    integer_value: Any
    boolean_value: Any
    string_value: Any
    double_value: Any
    price_value: Any
    integer_values: Any
    boolean_values: Any
    string_values: Any
    double_values: Any

class FeedItemPlaceholderPolicyInfo(proto.Message):
    placeholder_type_enum: Any
    feed_mapping_resource_name: Any
    review_status: Any
    approval_status: Any
    policy_topic_entries: Any
    validation_status: Any
    validation_errors: Any
    quality_approval_status: Any
    quality_disapproval_reasons: Any

class FeedItemValidationError(proto.Message):
    validation_error: Any
    description: Any
    feed_attribute_ids: Any
    extra_info: Any
