from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        call_conversion_action: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "call_reporting_enabled",
            "call_conversion_reporting_enabled",
            "call_conversion_action",
        ],
    ) -> bool: ...

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
        google_ads_conversion_customer: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "conversion_tracking_id",
            "cross_account_conversion_tracking_id",
            "accepted_customer_data_terms",
            "conversion_tracking_status",
            "enhanced_conversions_for_leads_enabled",
            "google_ads_conversion_customer",
        ],
    ) -> bool: ...

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
    customer_agreement_setting: CustomerAgreementSetting
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
        offline_conversion_client_summaries: MutableSequence[
            OfflineConversionClientSummary
        ] = ...,
        customer_agreement_setting: CustomerAgreementSetting = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "descriptive_name",
            "currency_code",
            "time_zone",
            "tracking_url_template",
            "final_url_suffix",
            "auto_tagging_enabled",
            "has_partners_badge",
            "manager",
            "test_account",
            "call_reporting_setting",
            "conversion_tracking_setting",
            "remarketing_setting",
            "pay_per_conversion_eligibility_failure_reasons",
            "optimization_score",
            "optimization_score_weight",
            "status",
            "location_asset_auto_migration_done",
            "image_asset_auto_migration_done",
            "location_asset_auto_migration_done_date_time",
            "image_asset_auto_migration_done_date_time",
            "offline_conversion_client_summaries",
            "customer_agreement_setting",
        ],
    ) -> bool: ...

class CustomerAgreementSetting(proto.Message):
    accepted_lead_form_terms: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        accepted_lead_form_terms: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["accepted_lead_form_terms"]
    ) -> bool: ...

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        client: OfflineEventUploadClientEnum.OfflineEventUploadClient = ...,
        status: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus = ...,
        total_event_count: int = ...,
        successful_event_count: int = ...,
        success_rate: float = ...,
        last_upload_date_time: str = ...,
        daily_summaries: MutableSequence[OfflineConversionUploadSummary] = ...,
        job_summaries: MutableSequence[OfflineConversionUploadSummary] = ...,
        alerts: MutableSequence[OfflineConversionUploadAlert] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "client",
            "status",
            "total_event_count",
            "successful_event_count",
            "success_rate",
            "last_upload_date_time",
            "daily_summaries",
            "job_summaries",
            "alerts",
        ],
    ) -> bool: ...

class OfflineConversionUploadAlert(proto.Message):
    error: OfflineConversionUploadError
    error_percentage: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        error: OfflineConversionUploadError = ...,
        error_percentage: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["error", "error_percentage"]
    ) -> bool: ...

class OfflineConversionUploadError(proto.Message):
    collection_size_error: CollectionSizeErrorEnum.CollectionSizeError
    conversion_adjustment_upload_error: (
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    )
    conversion_upload_error: ConversionUploadErrorEnum.ConversionUploadError
    date_error: DateErrorEnum.DateError
    distinct_error: DistinctErrorEnum.DistinctError
    field_error: FieldErrorEnum.FieldError
    mutate_error: MutateErrorEnum.MutateError
    not_allowlisted_error: NotAllowlistedErrorEnum.NotAllowlistedError
    string_format_error: StringFormatErrorEnum.StringFormatError
    string_length_error: StringLengthErrorEnum.StringLengthError
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        collection_size_error: CollectionSizeErrorEnum.CollectionSizeError = ...,
        conversion_adjustment_upload_error: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError = ...,
        conversion_upload_error: ConversionUploadErrorEnum.ConversionUploadError = ...,
        date_error: DateErrorEnum.DateError = ...,
        distinct_error: DistinctErrorEnum.DistinctError = ...,
        field_error: FieldErrorEnum.FieldError = ...,
        mutate_error: MutateErrorEnum.MutateError = ...,
        not_allowlisted_error: NotAllowlistedErrorEnum.NotAllowlistedError = ...,
        string_format_error: StringFormatErrorEnum.StringFormatError = ...,
        string_length_error: StringLengthErrorEnum.StringLengthError = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "collection_size_error",
            "conversion_adjustment_upload_error",
            "conversion_upload_error",
            "date_error",
            "distinct_error",
            "field_error",
            "mutate_error",
            "not_allowlisted_error",
            "string_format_error",
            "string_length_error",
        ],
    ) -> bool: ...

class OfflineConversionUploadSummary(proto.Message):
    successful_count: int
    failed_count: int
    job_id: int
    upload_date: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        successful_count: int = ...,
        failed_count: int = ...,
        job_id: int = ...,
        upload_date: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["successful_count", "failed_count", "job_id", "upload_date"]
    ) -> bool: ...

class RemarketingSetting(proto.Message):
    google_global_site_tag: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        google_global_site_tag: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["google_global_site_tag"]
    ) -> bool: ...
