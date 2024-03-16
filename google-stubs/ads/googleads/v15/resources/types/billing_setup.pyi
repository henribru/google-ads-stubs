from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.billing_setup_status import (
    BillingSetupStatusEnum,
)
from google.ads.googleads.v15.enums.types.time_type import TimeTypeEnum

_M = TypeVar("_M")

class BillingSetup(proto.Message):
    class PaymentsAccountInfo(proto.Message):
        payments_account_id: str
        payments_account_name: str
        payments_profile_id: str
        payments_profile_name: str
        secondary_payments_profile_id: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            payments_account_id: str = ...,
            payments_account_name: str = ...,
            payments_profile_id: str = ...,
            payments_profile_name: str = ...,
            secondary_payments_profile_id: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "payments_account_id",
                "payments_account_name",
                "payments_profile_id",
                "payments_profile_name",
                "secondary_payments_profile_id",
            ],
        ) -> bool: ...

    resource_name: str
    id: int
    status: BillingSetupStatusEnum.BillingSetupStatus
    payments_account: str
    payments_account_info: BillingSetup.PaymentsAccountInfo
    start_date_time: str
    start_time_type: TimeTypeEnum.TimeType
    end_date_time: str
    end_time_type: TimeTypeEnum.TimeType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        status: BillingSetupStatusEnum.BillingSetupStatus = ...,
        payments_account: str = ...,
        payments_account_info: BillingSetup.PaymentsAccountInfo = ...,
        start_date_time: str = ...,
        start_time_type: TimeTypeEnum.TimeType = ...,
        end_date_time: str = ...,
        end_time_type: TimeTypeEnum.TimeType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "status",
            "payments_account",
            "payments_account_info",
            "start_date_time",
            "start_time_type",
            "end_date_time",
            "end_time_type",
        ],
    ) -> bool: ...
