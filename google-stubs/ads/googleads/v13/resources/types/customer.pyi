from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.conversion_tracking_status_enum import (
    ConversionTrackingStatusEnum,
)
from google.ads.googleads.v13.enums.types.customer_pay_per_conversion_eligibility_failure_reason import (
    CustomerPayPerConversionEligibilityFailureReasonEnum,
)
from google.ads.googleads.v13.enums.types.customer_status import CustomerStatusEnum

_M = TypeVar("_M")

class CallReportingSetting(proto.Message):
    call_reporting_enabled: bool
    call_conversion_reporting_enabled: bool
    call_conversion_action: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        call_reporting_enabled: bool = ...,
        call_conversion_reporting_enabled: bool = ...,
        call_conversion_action: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["call_reporting_enabled", "call_conversion_reporting_enabled", "call_conversion_action"]) -> bool: ...  # type: ignore[override]

class ConversionTrackingSetting(proto.Message):
    conversion_tracking_id: int
    cross_account_conversion_tracking_id: int
    accepted_customer_data_terms: bool
    conversion_tracking_status: ConversionTrackingStatusEnum.ConversionTrackingStatus
    enhanced_conversions_for_leads_enabled: bool
    google_ads_conversion_customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        conversion_tracking_id: int = ...,
        cross_account_conversion_tracking_id: int = ...,
        accepted_customer_data_terms: bool = ...,
        conversion_tracking_status: ConversionTrackingStatusEnum.ConversionTrackingStatus = ...,
        enhanced_conversions_for_leads_enabled: bool = ...,
        google_ads_conversion_customer: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["conversion_tracking_id", "cross_account_conversion_tracking_id", "accepted_customer_data_terms", "conversion_tracking_status", "enhanced_conversions_for_leads_enabled", "google_ads_conversion_customer"]) -> bool: ...  # type: ignore[override]

class Customer(proto.Message):
    resource_name: str
    id: int
    descriptive_name: str
    currency_code: str
    time_zone: str
    tracking_url_template: str
    final_url_suffix: str
    auto_tagging_enabled: bool
    has_partners_badge: bool
    manager: bool
    test_account: bool
    call_reporting_setting: CallReportingSetting
    conversion_tracking_setting: ConversionTrackingSetting
    remarketing_setting: RemarketingSetting
    pay_per_conversion_eligibility_failure_reasons: MutableSequence[
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    ]
    optimization_score: float
    optimization_score_weight: float
    status: CustomerStatusEnum.CustomerStatus
    location_asset_auto_migration_done: bool
    image_asset_auto_migration_done: bool
    location_asset_auto_migration_done_date_time: str
    image_asset_auto_migration_done_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        descriptive_name: str = ...,
        currency_code: str = ...,
        time_zone: str = ...,
        tracking_url_template: str = ...,
        final_url_suffix: str = ...,
        auto_tagging_enabled: bool = ...,
        has_partners_badge: bool = ...,
        manager: bool = ...,
        test_account: bool = ...,
        call_reporting_setting: CallReportingSetting = ...,
        conversion_tracking_setting: ConversionTrackingSetting = ...,
        remarketing_setting: RemarketingSetting = ...,
        pay_per_conversion_eligibility_failure_reasons: MutableSequence[
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
        ] = ...,
        optimization_score: float = ...,
        optimization_score_weight: float = ...,
        status: CustomerStatusEnum.CustomerStatus = ...,
        location_asset_auto_migration_done: bool = ...,
        image_asset_auto_migration_done: bool = ...,
        location_asset_auto_migration_done_date_time: str = ...,
        image_asset_auto_migration_done_date_time: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "id", "descriptive_name", "currency_code", "time_zone", "tracking_url_template", "final_url_suffix", "auto_tagging_enabled", "has_partners_badge", "manager", "test_account", "call_reporting_setting", "conversion_tracking_setting", "remarketing_setting", "pay_per_conversion_eligibility_failure_reasons", "optimization_score", "optimization_score_weight", "status", "location_asset_auto_migration_done", "image_asset_auto_migration_done", "location_asset_auto_migration_done_date_time", "image_asset_auto_migration_done_date_time"]) -> bool: ...  # type: ignore[override]

class RemarketingSetting(proto.Message):
    google_global_site_tag: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        google_global_site_tag: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["google_global_site_tag"]) -> bool: ...  # type: ignore[override]
