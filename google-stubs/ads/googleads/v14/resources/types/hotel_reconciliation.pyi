from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.hotel_reconciliation_status import (
    HotelReconciliationStatusEnum,
)

_M = TypeVar("_M")

class HotelReconciliation(proto.Message):
    resource_name: str
    commission_id: str
    order_id: str
    campaign: str
    hotel_center_id: int
    hotel_id: str
    check_in_date: str
    check_out_date: str
    reconciled_value_micros: int
    billed: bool
    status: HotelReconciliationStatusEnum.HotelReconciliationStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        commission_id: str = ...,
        order_id: str = ...,
        campaign: str = ...,
        hotel_center_id: int = ...,
        hotel_id: str = ...,
        check_in_date: str = ...,
        check_out_date: str = ...,
        reconciled_value_micros: int = ...,
        billed: bool = ...,
        status: HotelReconciliationStatusEnum.HotelReconciliationStatus = ...
    ) -> None: ...
