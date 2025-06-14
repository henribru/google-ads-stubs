import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import offline_conversion_diagnostic_status_enum, offline_event_upload_client_enum
from google.ads.googleads.v20.resources.types import offline_conversion_upload_client_summary
from typing import MutableSequence

__protobuf__: Incomplete

class OfflineConversionUploadConversionActionSummary(proto.Message):
    resource_name: str
    client: offline_event_upload_client_enum.OfflineEventUploadClientEnum.OfflineEventUploadClient
    conversion_action_id: int
    conversion_action_name: str
    status: offline_conversion_diagnostic_status_enum.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    total_event_count: int
    successful_event_count: int
    pending_event_count: int
    last_upload_date_time: str
    daily_summaries: MutableSequence[offline_conversion_upload_client_summary.OfflineConversionSummary]
    job_summaries: MutableSequence[offline_conversion_upload_client_summary.OfflineConversionSummary]
    alerts: MutableSequence[offline_conversion_upload_client_summary.OfflineConversionAlert]
