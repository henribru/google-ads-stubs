from typing import Any

import proto

from google.ads.googleads.v9.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v9.enums.types import (
    offline_user_data_job_failure_reason as offline_user_data_job_failure_reason,
    offline_user_data_job_match_rate_range as offline_user_data_job_match_rate_range,
    offline_user_data_job_status as offline_user_data_job_status,
    offline_user_data_job_type as offline_user_data_job_type,
)

__protobuf__: Any

class OfflineUserDataJob(proto.Message):
    resource_name: Any
    id: Any
    external_id: Any
    type_: Any
    status: Any
    failure_reason: Any
    operation_metadata: Any
    customer_match_user_list_metadata: Any
    store_sales_metadata: Any

class OfflineUserDataJobMetadata(proto.Message):
    match_rate_range: Any
