import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import brand_safety_suitability, conversion_tracking_status_enum, customer_pay_per_conversion_eligibility_failure_reason, customer_status, local_services_verification_status
from typing import MutableSequence

__protobuf__: Incomplete

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
    pay_per_conversion_eligibility_failure_reasons: MutableSequence[customer_pay_per_conversion_eligibility_failure_reason.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
    optimization_score: float
    optimization_score_weight: float
    status: customer_status.CustomerStatusEnum.CustomerStatus
    location_asset_auto_migration_done: bool
    image_asset_auto_migration_done: bool
    location_asset_auto_migration_done_date_time: str
    image_asset_auto_migration_done_date_time: str
    customer_agreement_setting: CustomerAgreementSetting
    local_services_settings: LocalServicesSettings
    video_brand_safety_suitability: brand_safety_suitability.BrandSafetySuitabilityEnum.BrandSafetySuitability

class CallReportingSetting(proto.Message):
    call_reporting_enabled: bool
    call_conversion_reporting_enabled: bool
    call_conversion_action: str

class ConversionTrackingSetting(proto.Message):
    conversion_tracking_id: int
    cross_account_conversion_tracking_id: int
    accepted_customer_data_terms: bool
    conversion_tracking_status: conversion_tracking_status_enum.ConversionTrackingStatusEnum.ConversionTrackingStatus
    enhanced_conversions_for_leads_enabled: bool
    google_ads_conversion_customer: str

class RemarketingSetting(proto.Message):
    google_global_site_tag: str

class CustomerAgreementSetting(proto.Message):
    accepted_lead_form_terms: bool

class LocalServicesSettings(proto.Message):
    granular_license_statuses: MutableSequence['GranularLicenseStatus']
    granular_insurance_statuses: MutableSequence['GranularInsuranceStatus']

class GranularLicenseStatus(proto.Message):
    geo_criterion_id: int
    category_id: str
    verification_status: local_services_verification_status.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus

class GranularInsuranceStatus(proto.Message):
    geo_criterion_id: int
    category_id: str
    verification_status: local_services_verification_status.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
