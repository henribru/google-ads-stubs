from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.offline_user_data import (
    CustomerMatchUserListMetadata,
    StoreSalesMetadata,
)
from google.ads.googleads.v14.enums.types.offline_user_data_job_failure_reason import (
    OfflineUserDataJobFailureReasonEnum,
)
from google.ads.googleads.v14.enums.types.offline_user_data_job_match_rate_range import (
    OfflineUserDataJobMatchRateRangeEnum,
)
from google.ads.googleads.v14.enums.types.offline_user_data_job_status import (
    OfflineUserDataJobStatusEnum,
)
from google.ads.googleads.v14.enums.types.offline_user_data_job_type import (
    OfflineUserDataJobTypeEnum,
)

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        external_id: int = ...,
        type_: OfflineUserDataJobTypeEnum.OfflineUserDataJobType = ...,
        status: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus = ...,
        failure_reason: OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason = ...,
        operation_metadata: OfflineUserDataJobMetadata = ...,
        customer_match_user_list_metadata: CustomerMatchUserListMetadata = ...,
        store_sales_metadata: StoreSalesMetadata = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "external_id",
            "type_",
            "status",
            "failure_reason",
            "operation_metadata",
            "customer_match_user_list_metadata",
            "store_sales_metadata",
        ],
    ) -> bool: ...

class OfflineUserDataJobMetadata(proto.Message):
    match_rate_range: (
        OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange
    )
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        match_rate_range: OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["match_rate_range"]
    ) -> bool: ...
