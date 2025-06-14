import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import offline_user_data
from google.ads.googleads.v20.enums.types import offline_user_data_job_failure_reason, offline_user_data_job_match_rate_range, offline_user_data_job_status, offline_user_data_job_type

__protobuf__: Incomplete

class OfflineUserDataJob(proto.Message):
    resource_name: str
    id: int
    external_id: int
    type_: offline_user_data_job_type.OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    status: offline_user_data_job_status.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    failure_reason: offline_user_data_job_failure_reason.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    operation_metadata: OfflineUserDataJobMetadata
    customer_match_user_list_metadata: offline_user_data.CustomerMatchUserListMetadata
    store_sales_metadata: offline_user_data.StoreSalesMetadata

class OfflineUserDataJobMetadata(proto.Message):
    match_rate_range: offline_user_data_job_match_rate_range.OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange
