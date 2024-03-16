from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.offline_conversion_diagnostic_status_enum import (
    OfflineConversionDiagnosticStatusEnum,
)
from google.ads.googleads.v16.enums.types.offline_event_upload_client_enum import (
    OfflineEventUploadClientEnum,
)
from google.ads.googleads.v16.errors.types.collection_size_error import (
    CollectionSizeErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_adjustment_upload_error import (
    ConversionAdjustmentUploadErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_upload_error import (
    ConversionUploadErrorEnum,
)
from google.ads.googleads.v16.errors.types.date_error import DateErrorEnum
from google.ads.googleads.v16.errors.types.distinct_error import DistinctErrorEnum
from google.ads.googleads.v16.errors.types.field_error import FieldErrorEnum
from google.ads.googleads.v16.errors.types.mutate_error import MutateErrorEnum
from google.ads.googleads.v16.errors.types.not_allowlisted_error import (
    NotAllowlistedErrorEnum,
)
from google.ads.googleads.v16.errors.types.string_format_error import (
    StringFormatErrorEnum,
)
from google.ads.googleads.v16.errors.types.string_length_error import (
    StringLengthErrorEnum,
)

_M = TypeVar("_M")

class OfflineConversionAlert(proto.Message):
    error: OfflineConversionError
    error_percentage: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        error: OfflineConversionError = ...,
        error_percentage: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["error", "error_percentage"]
    ) -> bool: ...

class OfflineConversionError(proto.Message):
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

class OfflineConversionSummary(proto.Message):
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

class OfflineConversionUploadClientSummary(proto.Message):
    resource_name: str
    client: OfflineEventUploadClientEnum.OfflineEventUploadClient
    status: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    total_event_count: int
    successful_event_count: int
    success_rate: float
    last_upload_date_time: str
    daily_summaries: MutableSequence[OfflineConversionSummary]
    job_summaries: MutableSequence[OfflineConversionSummary]
    alerts: MutableSequence[OfflineConversionAlert]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        client: OfflineEventUploadClientEnum.OfflineEventUploadClient = ...,
        status: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus = ...,
        total_event_count: int = ...,
        successful_event_count: int = ...,
        success_rate: float = ...,
        last_upload_date_time: str = ...,
        daily_summaries: MutableSequence[OfflineConversionSummary] = ...,
        job_summaries: MutableSequence[OfflineConversionSummary] = ...,
        alerts: MutableSequence[OfflineConversionAlert] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
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
