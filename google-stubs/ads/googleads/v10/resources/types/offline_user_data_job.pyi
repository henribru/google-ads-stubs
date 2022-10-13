from typing import Any

import proto

from google.ads.googleads.v10.common.types.offline_user_data import (
    CustomerMatchUserListMetadata,
    StoreSalesMetadata,
)
from google.ads.googleads.v10.enums.types.offline_user_data_job_failure_reason import (
    OfflineUserDataJobFailureReasonEnum,
)
from google.ads.googleads.v10.enums.types.offline_user_data_job_match_rate_range import (
    OfflineUserDataJobMatchRateRangeEnum,
)
from google.ads.googleads.v10.enums.types.offline_user_data_job_status import (
    OfflineUserDataJobStatusEnum,
)
from google.ads.googleads.v10.enums.types.offline_user_data_job_type import (
    OfflineUserDataJobTypeEnum,
)

class OfflineUserDataJob(proto.Message):
    resource_name: str
    id: int
    external_id: int
    type_: OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    status: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    failure_reason: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    operation_metadata: OfflineUserDataJobMetadata
    customer_match_user_list_metadata: CustomerMatchUserListMetadata
    store_sales_metadata: StoreSalesMetadata
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        external_id: int = ...,
        type_: OfflineUserDataJobTypeEnum.OfflineUserDataJobType = ...,
        status: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus = ...,
        failure_reason: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason = ...,
        operation_metadata: OfflineUserDataJobMetadata = ...,
        customer_match_user_list_metadata: CustomerMatchUserListMetadata = ...,
        store_sales_metadata: StoreSalesMetadata = ...
    ) -> None: ...

class OfflineUserDataJobMetadata(proto.Message):
    match_rate_range: OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        match_rate_range: OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange = ...
    ) -> None: ...
