from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v19.enums.types.offline_conversion_diagnostic_status_enum import (
    OfflineConversionDiagnosticStatusEnum,
)
from google.ads.googleads.v19.enums.types.offline_event_upload_client_enum import (
    OfflineEventUploadClientEnum,
)
from google.ads.googleads.v19.resources.types.offline_conversion_upload_client_summary import (
    OfflineConversionAlert,
    OfflineConversionSummary,
)

_M = TypeVar("_M")

class OfflineConversionUploadConversionActionSummary(proto.Message):
    resource_name: str
    client: OfflineEventUploadClientEnum.OfflineEventUploadClient
    conversion_action_id: int
    conversion_action_name: str
    status: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    total_event_count: int
    successful_event_count: int
    pending_event_count: int
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
        conversion_action_id: int = ...,
        conversion_action_name: str = ...,
        status: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus = ...,
        total_event_count: int = ...,
        successful_event_count: int = ...,
        pending_event_count: int = ...,
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
            "conversion_action_id",
            "conversion_action_name",
            "status",
            "total_event_count",
            "successful_event_count",
            "pending_event_count",
            "last_upload_date_time",
            "daily_summaries",
            "job_summaries",
            "alerts",
        ],
    ) -> bool: ...
