from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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
            secondary_payments_profile_id: str = ...
        ) -> None: ...
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
        end_time_type: TimeTypeEnum.TimeType = ...
    ) -> None: ...
