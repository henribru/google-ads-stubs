from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.hotel_reconciliation_status import (
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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        status: HotelReconciliationStatusEnum.HotelReconciliationStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "commission_id",
            "order_id",
            "campaign",
            "hotel_center_id",
            "hotel_id",
            "check_in_date",
            "check_out_date",
            "reconciled_value_micros",
            "billed",
            "status",
        ],
    ) -> bool: ...
