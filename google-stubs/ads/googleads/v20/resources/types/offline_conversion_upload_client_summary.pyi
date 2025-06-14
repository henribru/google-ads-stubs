import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import offline_conversion_diagnostic_status_enum, offline_event_upload_client_enum
from google.ads.googleads.v20.errors.types import collection_size_error as gage_collection_size_error, conversion_adjustment_upload_error as gage_conversion_adjustment_upload_error, conversion_upload_error as gage_conversion_upload_error, date_error as gage_date_error, distinct_error as gage_distinct_error, field_error as gage_field_error, mutate_error as gage_mutate_error, not_allowlisted_error as gage_not_allowlisted_error, string_format_error as gage_string_format_error, string_length_error as gage_string_length_error
from typing import MutableSequence

__protobuf__: Incomplete

class OfflineConversionUploadClientSummary(proto.Message):
    resource_name: str
    client: offline_event_upload_client_enum.OfflineEventUploadClientEnum.OfflineEventUploadClient
    status: offline_conversion_diagnostic_status_enum.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    total_event_count: int
    successful_event_count: int
    success_rate: float
    pending_event_count: int
    pending_rate: float
    last_upload_date_time: str
    daily_summaries: MutableSequence['OfflineConversionSummary']
    job_summaries: MutableSequence['OfflineConversionSummary']
    alerts: MutableSequence['OfflineConversionAlert']

class OfflineConversionSummary(proto.Message):
    successful_count: int
    failed_count: int
    pending_count: int
    job_id: int
    upload_date: str

class OfflineConversionAlert(proto.Message):
    error: OfflineConversionError
    error_percentage: float

class OfflineConversionError(proto.Message):
    collection_size_error: gage_collection_size_error.CollectionSizeErrorEnum.CollectionSizeError
    conversion_adjustment_upload_error: gage_conversion_adjustment_upload_error.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    conversion_upload_error: gage_conversion_upload_error.ConversionUploadErrorEnum.ConversionUploadError
    date_error: gage_date_error.DateErrorEnum.DateError
    distinct_error: gage_distinct_error.DistinctErrorEnum.DistinctError
    field_error: gage_field_error.FieldErrorEnum.FieldError
    mutate_error: gage_mutate_error.MutateErrorEnum.MutateError
    not_allowlisted_error: gage_not_allowlisted_error.NotAllowlistedErrorEnum.NotAllowlistedError
    string_format_error: gage_string_format_error.StringFormatErrorEnum.StringFormatError
    string_length_error: gage_string_length_error.StringLengthErrorEnum.StringLengthError
