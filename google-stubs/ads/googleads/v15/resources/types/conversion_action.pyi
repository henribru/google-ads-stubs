from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.tag_snippet import TagSnippet
from google.ads.googleads.v15.enums.types.attribution_model import AttributionModelEnum
from google.ads.googleads.v15.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v15.enums.types.conversion_action_counting_type import (
    ConversionActionCountingTypeEnum,
)
from google.ads.googleads.v15.enums.types.conversion_action_status import (
    ConversionActionStatusEnum,
)
from google.ads.googleads.v15.enums.types.conversion_action_type import (
    ConversionActionTypeEnum,
)
from google.ads.googleads.v15.enums.types.conversion_origin import ConversionOriginEnum
from google.ads.googleads.v15.enums.types.data_driven_model_status import (
    DataDrivenModelStatusEnum,
)
from google.ads.googleads.v15.enums.types.mobile_app_vendor import MobileAppVendorEnum

_M = TypeVar("_M")

class ConversionAction(proto.Message):
    class AttributionModelSettings(proto.Message):
        attribution_model: AttributionModelEnum.AttributionModel
        data_driven_model_status: DataDrivenModelStatusEnum.DataDrivenModelStatus
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            attribution_model: AttributionModelEnum.AttributionModel = ...,
            data_driven_model_status: DataDrivenModelStatusEnum.DataDrivenModelStatus = ...
        ) -> None: ...

    class FirebaseSettings(proto.Message):
        event_name: str
        project_id: str
        property_id: int
        property_name: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            event_name: str = ...,
            project_id: str = ...,
            property_id: int = ...,
            property_name: str = ...
        ) -> None: ...

    class GoogleAnalytics4Settings(proto.Message):
        event_name: str
        property_name: str
        property_id: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            event_name: str = ...,
            property_name: str = ...,
            property_id: int = ...
        ) -> None: ...

    class ThirdPartyAppAnalyticsSettings(proto.Message):
        event_name: str
        provider_name: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            event_name: str = ...,
            provider_name: str = ...
        ) -> None: ...

    class ValueSettings(proto.Message):
        default_value: float
        default_currency_code: str
        always_use_default_value: bool
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            default_value: float = ...,
            default_currency_code: str = ...,
            always_use_default_value: bool = ...
        ) -> None: ...
    resource_name: str
    id: int
    name: str
    status: ConversionActionStatusEnum.ConversionActionStatus
    type_: ConversionActionTypeEnum.ConversionActionType
    origin: ConversionOriginEnum.ConversionOrigin
    primary_for_goal: bool
    category: ConversionActionCategoryEnum.ConversionActionCategory
    owner_customer: str
    include_in_conversions_metric: bool
    click_through_lookback_window_days: int
    view_through_lookback_window_days: int
    value_settings: ConversionAction.ValueSettings
    counting_type: ConversionActionCountingTypeEnum.ConversionActionCountingType
    attribution_model_settings: ConversionAction.AttributionModelSettings
    tag_snippets: MutableSequence[TagSnippet]
    phone_call_duration_seconds: int
    app_id: str
    mobile_app_vendor: MobileAppVendorEnum.MobileAppVendor
    firebase_settings: ConversionAction.FirebaseSettings
    third_party_app_analytics_settings: ConversionAction.ThirdPartyAppAnalyticsSettings
    google_analytics_4_settings: ConversionAction.GoogleAnalytics4Settings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: ConversionActionStatusEnum.ConversionActionStatus = ...,
        type_: ConversionActionTypeEnum.ConversionActionType = ...,
        origin: ConversionOriginEnum.ConversionOrigin = ...,
        primary_for_goal: bool = ...,
        category: ConversionActionCategoryEnum.ConversionActionCategory = ...,
        owner_customer: str = ...,
        include_in_conversions_metric: bool = ...,
        click_through_lookback_window_days: int = ...,
        view_through_lookback_window_days: int = ...,
        value_settings: ConversionAction.ValueSettings = ...,
        counting_type: ConversionActionCountingTypeEnum.ConversionActionCountingType = ...,
        attribution_model_settings: ConversionAction.AttributionModelSettings = ...,
        tag_snippets: MutableSequence[TagSnippet] = ...,
        phone_call_duration_seconds: int = ...,
        app_id: str = ...,
        mobile_app_vendor: MobileAppVendorEnum.MobileAppVendor = ...,
        firebase_settings: ConversionAction.FirebaseSettings = ...,
        third_party_app_analytics_settings: ConversionAction.ThirdPartyAppAnalyticsSettings = ...,
        google_analytics_4_settings: ConversionAction.GoogleAnalytics4Settings = ...
    ) -> None: ...
