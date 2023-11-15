from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.conversion_tracking_status_enum import (
    ConversionTrackingStatusEnum,
)
from google.ads.googleads.v15.enums.types.customer_pay_per_conversion_eligibility_failure_reason import (
    CustomerPayPerConversionEligibilityFailureReasonEnum,
)
from google.ads.googleads.v15.enums.types.customer_status import CustomerStatusEnum
from google.ads.googleads.v15.enums.types.local_services_verification_status import (
    LocalServicesVerificationStatusEnum,
)

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
    customer_agreement_setting: CustomerAgreementSetting
    local_services_settings: LocalServicesSettings
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
        image_asset_auto_migration_done_date_time: str = ...,
        customer_agreement_setting: CustomerAgreementSetting = ...,
        local_services_settings: LocalServicesSettings = ...
    ) -> None: ...

class CustomerAgreementSetting(proto.Message):
    accepted_lead_form_terms: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        accepted_lead_form_terms: bool = ...
    ) -> None: ...

class GranularInsuranceStatus(proto.Message):
    geo_criterion_id: int
    category_id: str
    verification_status: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_criterion_id: int = ...,
        category_id: str = ...,
        verification_status: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus = ...
    ) -> None: ...

class GranularLicenseStatus(proto.Message):
    geo_criterion_id: int
    category_id: str
    verification_status: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_criterion_id: int = ...,
        category_id: str = ...,
        verification_status: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus = ...
    ) -> None: ...

class LocalServicesSettings(proto.Message):
    granular_license_statuses: MutableSequence[GranularLicenseStatus]
    granular_insurance_statuses: MutableSequence[GranularInsuranceStatus]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        granular_license_statuses: MutableSequence[GranularLicenseStatus] = ...,
        granular_insurance_statuses: MutableSequence[GranularInsuranceStatus] = ...
    ) -> None: ...

class RemarketingSetting(proto.Message):
    google_global_site_tag: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        google_global_site_tag: str = ...
    ) -> None: ...
