from typing import Any

import proto

from google.ads.googleads.v8.common.types import tag_snippet as tag_snippet
from google.ads.googleads.v8.enums.types import (
    conversion_action_category as conversion_action_category,
    conversion_action_counting_type as conversion_action_counting_type,
    conversion_action_status as conversion_action_status,
    conversion_action_type as conversion_action_type,
)

__protobuf__: Any

class ConversionAction(proto.Message):
    class AttributionModelSettings(proto.Message):
        attribution_model: Any
        data_driven_model_status: Any
    class ValueSettings(proto.Message):
        default_value: Any
        default_currency_code: Any
        always_use_default_value: Any
    class ThirdPartyAppAnalyticsSettings(proto.Message):
        event_name: Any
        provider_name: Any
    class FirebaseSettings(proto.Message):
        event_name: Any
        project_id: Any
    resource_name: Any
    id: Any
    name: Any
    status: Any
    type_: Any
    category: Any
    owner_customer: Any
    include_in_conversions_metric: Any
    click_through_lookback_window_days: Any
    view_through_lookback_window_days: Any
    value_settings: Any
    counting_type: Any
    attribution_model_settings: Any
    tag_snippets: Any
    phone_call_duration_seconds: Any
    app_id: Any
    mobile_app_vendor: Any
    firebase_settings: Any
    third_party_app_analytics_settings: Any