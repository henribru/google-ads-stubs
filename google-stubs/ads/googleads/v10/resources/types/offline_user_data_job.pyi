import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v10.enums.types import (
    offline_user_data_job_failure_reason as offline_user_data_job_failure_reason,
    offline_user_data_job_match_rate_range as offline_user_data_job_match_rate_range,
    offline_user_data_job_status as offline_user_data_job_status,
    offline_user_data_job_type as offline_user_data_job_type,
)

__protobuf__: Incomplete

class OfflineUserDataJob(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    external_id: Incomplete
    type_: Incomplete
    status: Incomplete
    failure_reason: Incomplete
    operation_metadata: Incomplete
    customer_match_user_list_metadata: Incomplete
    store_sales_metadata: Incomplete

class OfflineUserDataJobMetadata(proto.Message):
    match_rate_range: Incomplete
