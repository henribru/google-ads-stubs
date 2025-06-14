import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import tag_snippet
from google.ads.googleads.v19.enums.types import attribution_model as gage_attribution_model, conversion_action_category, conversion_action_counting_type, conversion_action_status, conversion_action_type, conversion_origin, data_driven_model_status as gage_data_driven_model_status, mobile_app_vendor as gage_mobile_app_vendor
from typing import MutableSequence

__protobuf__: Incomplete

class ConversionAction(proto.Message):
    class AttributionModelSettings(proto.Message):
        attribution_model: gage_attribution_model.AttributionModelEnum.AttributionModel
        data_driven_model_status: gage_data_driven_model_status.DataDrivenModelStatusEnum.DataDrivenModelStatus
    class ValueSettings(proto.Message):
        default_value: float
        default_currency_code: str
        always_use_default_value: bool
    class ThirdPartyAppAnalyticsSettings(proto.Message):
        event_name: str
        provider_name: str
    class FirebaseSettings(proto.Message):
        event_name: str
        project_id: str
        property_id: int
        property_name: str
    class GoogleAnalytics4Settings(proto.Message):
        event_name: str
        property_name: str
        property_id: int
    resource_name: str
    id: int
    name: str
    status: conversion_action_status.ConversionActionStatusEnum.ConversionActionStatus
    type_: conversion_action_type.ConversionActionTypeEnum.ConversionActionType
    origin: conversion_origin.ConversionOriginEnum.ConversionOrigin
    primary_for_goal: bool
    category: conversion_action_category.ConversionActionCategoryEnum.ConversionActionCategory
    owner_customer: str
    include_in_conversions_metric: bool
    click_through_lookback_window_days: int
    view_through_lookback_window_days: int
    value_settings: ValueSettings
    counting_type: conversion_action_counting_type.ConversionActionCountingTypeEnum.ConversionActionCountingType
    attribution_model_settings: AttributionModelSettings
    tag_snippets: MutableSequence[tag_snippet.TagSnippet]
    phone_call_duration_seconds: int
    app_id: str
    mobile_app_vendor: gage_mobile_app_vendor.MobileAppVendorEnum.MobileAppVendor
    firebase_settings: FirebaseSettings
    third_party_app_analytics_settings: ThirdPartyAppAnalyticsSettings
    google_analytics_4_settings: GoogleAnalytics4Settings
