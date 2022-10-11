import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import tag_snippet as tag_snippet
from google.ads.googleads.v11.enums.types import (
    conversion_action_category as conversion_action_category,
    conversion_action_counting_type as conversion_action_counting_type,
    conversion_action_status as conversion_action_status,
    conversion_action_type as conversion_action_type,
    conversion_origin as conversion_origin,
)

__protobuf__: Incomplete

class ConversionAction(proto.Message):
    class AttributionModelSettings(proto.Message):
        attribution_model: Incomplete
        data_driven_model_status: Incomplete

    class ValueSettings(proto.Message):
        default_value: Incomplete
        default_currency_code: Incomplete
        always_use_default_value: Incomplete

    class ThirdPartyAppAnalyticsSettings(proto.Message):
        event_name: Incomplete
        provider_name: Incomplete

    class FirebaseSettings(proto.Message):
        event_name: Incomplete
        project_id: Incomplete
        property_id: Incomplete
        property_name: Incomplete
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    status: Incomplete
    type_: Incomplete
    origin: Incomplete
    primary_for_goal: Incomplete
    category: Incomplete
    owner_customer: Incomplete
    include_in_conversions_metric: Incomplete
    click_through_lookback_window_days: Incomplete
    view_through_lookback_window_days: Incomplete
    value_settings: Incomplete
    counting_type: Incomplete
    attribution_model_settings: Incomplete
    tag_snippets: Incomplete
    phone_call_duration_seconds: Incomplete
    app_id: Incomplete
    mobile_app_vendor: Incomplete
    firebase_settings: Incomplete
    third_party_app_analytics_settings: Incomplete
