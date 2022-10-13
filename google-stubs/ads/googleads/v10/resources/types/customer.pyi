from typing import Any

import proto

from google.ads.googleads.v10.enums.types.conversion_tracking_status_enum import (
    ConversionTrackingStatusEnum,
)
from google.ads.googleads.v10.enums.types.customer_pay_per_conversion_eligibility_failure_reason import (
    CustomerPayPerConversionEligibilityFailureReasonEnum,
)
from google.ads.googleads.v10.enums.types.customer_status import CustomerStatusEnum

class CallReportingSetting(proto.Message):
    call_reporting_enabled: bool
    call_conversion_reporting_enabled: bool
    call_conversion_action: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        call_reporting_enabled: bool = ...,
        call_conversion_reporting_enabled: bool = ...,
        call_conversion_action: str = ...
    ) -> None: ...

class ConversionTrackingSetting(proto.Message):
    conversion_tracking_id: int
    cross_account_conversion_tracking_id: int
    accepted_customer_data_terms: bool
    conversion_tracking_status: ConversionTrackingStatusEnum.ConversionTrackingStatus
    enhanced_conversions_for_leads_enabled: bool
    google_ads_conversion_customer: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        conversion_tracking_id: int = ...,
        cross_account_conversion_tracking_id: int = ...,
        accepted_customer_data_terms: bool = ...,
        conversion_tracking_status: ConversionTrackingStatusEnum.ConversionTrackingStatus = ...,
        enhanced_conversions_for_leads_enabled: bool = ...,
        google_ads_conversion_customer: str = ...
    ) -> None: ...

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
    pay_per_conversion_eligibility_failure_reasons: list[
        CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    ]
    optimization_score: float
    optimization_score_weight: float
    status: CustomerStatusEnum.CustomerStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        pay_per_conversion_eligibility_failure_reasons: list[
            CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
        ] = ...,
        optimization_score: float = ...,
        optimization_score_weight: float = ...,
        status: CustomerStatusEnum.CustomerStatus = ...
    ) -> None: ...

class RemarketingSetting(proto.Message):
    google_global_site_tag: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        google_global_site_tag: str = ...
    ) -> None: ...
