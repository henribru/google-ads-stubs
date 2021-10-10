from typing import Any

import proto

from google.ads.googleads.v7.common.types import offline_user_data as offline_user_data
from google.ads.googleads.v7.enums.types import (
    offline_user_data_job_failure_reason as offline_user_data_job_failure_reason,
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
    customer_match_user_list_metadata: Any
    store_sales_metadata: Any
