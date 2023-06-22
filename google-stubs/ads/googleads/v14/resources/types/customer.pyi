from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v14.enums.types.conversion_tracking_status_enum import (
    ConversionTrackingStatusEnum,
)
from google.ads.googleads.v14.enums.types.customer_pay_per_conversion_eligibility_failure_reason import (
    CustomerPayPerConversionEligibilityFailureReasonEnum,
)
from google.ads.googleads.v14.enums.types.customer_status import CustomerStatusEnum
from google.ads.googleads.v14.enums.types.offline_conversion_diagnostic_status_enum import (
    OfflineConversionDiagnosticStatusEnum,
)
from google.ads.googleads.v14.enums.types.offline_event_upload_client_enum import (
    OfflineEventUploadClientEnum,
)
from google.ads.googleads.v14.errors.types.collection_size_error import (
    CollectionSizeErrorEnum,
)
from google.ads.googleads.v14.errors.types.conversion_adjustment_upload_error import (
    ConversionAdjustmentUploadErrorEnum,
)
from google.ads.googleads.v14.errors.types.conversion_upload_error import (
    ConversionUploadErrorEnum,
)
from google.ads.googleads.v14.errors.types.date_error import DateErrorEnum
from google.ads.googleads.v14.errors.types.distinct_error import DistinctErrorEnum
from google.ads.googleads.v14.errors.types.field_error import FieldErrorEnum
from google.ads.googleads.v14.errors.types.mutate_error import MutateErrorEnum
from google.ads.googleads.v14.errors.types.not_allowlisted_error import (
    NotAllowlistedErrorEnum,
)
from google.ads.googleads.v14.errors.types.string_format_error import (
    StringFormatErrorEnum,
)
from google.ads.googleads.v14.errors.types.string_length_error import (
    StringLengthErrorEnum,
)

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
    offline_conversion_client_summaries: MutableSequence[OfflineConversionClientSummary]
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
        offline_conversion_client_summaries: MutableSequence[
            OfflineConversionClientSummary
        ] = ...
    ) -> None: ...

class OfflineConversionClientSummary(proto.Message):
    client: OfflineEventUploadClientEnum.OfflineEventUploadClient
    status: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    total_event_count: int
    successful_event_count: int
    success_rate: float
    last_upload_date_time: str
    daily_summaries: MutableSequence[OfflineConversionUploadSummary]
    job_summaries: MutableSequence[OfflineConversionUploadSummary]
    alerts: MutableSequence[OfflineConversionUploadAlert]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        client: OfflineEventUploadClientEnum.OfflineEventUploadClient = ...,
        status: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus = ...,
        total_event_count: int = ...,
        successful_event_count: int = ...,
        success_rate: float = ...,
        last_upload_date_time: str = ...,
        daily_summaries: MutableSequence[OfflineConversionUploadSummary] = ...,
        job_summaries: MutableSequence[OfflineConversionUploadSummary] = ...,
        alerts: MutableSequence[OfflineConversionUploadAlert] = ...
    ) -> None: ...

class OfflineConversionUploadAlert(proto.Message):
    error: OfflineConversionUploadError
    error_percentage: float
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        error: OfflineConversionUploadError = ...,
        error_percentage: float = ...
    ) -> None: ...

class OfflineConversionUploadError(proto.Message):
    collection_size_error: CollectionSizeErrorEnum.CollectionSizeError
    conversion_adjustment_upload_error: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    conversion_upload_error: ConversionUploadErrorEnum.ConversionUploadError
    date_error: DateErrorEnum.DateError
    distinct_error: DistinctErrorEnum.DistinctError
    field_error: FieldErrorEnum.FieldError
    mutate_error: MutateErrorEnum.MutateError
    not_allowlisted_error: NotAllowlistedErrorEnum.NotAllowlistedError
    string_format_error: StringFormatErrorEnum.StringFormatError
    string_length_error: StringLengthErrorEnum.StringLengthError
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        collection_size_error: CollectionSizeErrorEnum.CollectionSizeError = ...,
        conversion_adjustment_upload_error: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError = ...,
        conversion_upload_error: ConversionUploadErrorEnum.ConversionUploadError = ...,
        date_error: DateErrorEnum.DateError = ...,
        distinct_error: DistinctErrorEnum.DistinctError = ...,
        field_error: FieldErrorEnum.FieldError = ...,
        mutate_error: MutateErrorEnum.MutateError = ...,
        not_allowlisted_error: NotAllowlistedErrorEnum.NotAllowlistedError = ...,
        string_format_error: StringFormatErrorEnum.StringFormatError = ...,
        string_length_error: StringLengthErrorEnum.StringLengthError = ...
    ) -> None: ...

class OfflineConversionUploadSummary(proto.Message):
    successful_count: int
    failed_count: int
    job_id: int
    upload_date: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        successful_count: int = ...,
        failed_count: int = ...,
        job_id: int = ...,
        upload_date: str = ...
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
