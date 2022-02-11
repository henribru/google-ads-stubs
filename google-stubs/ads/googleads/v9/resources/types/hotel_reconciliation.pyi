from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    hotel_reconciliation_status as hotel_reconciliation_status,
)

__protobuf__: Any

class HotelReconciliation(proto.Message):
    resource_name: Any
    commission_id: Any
    order_id: Any
    hotel_center_id: Any
    hotel_id: Any
    check_in_date: Any
    check_out_date: Any
    reconciled_value_micros: Any
    billed: Any
    status: Any
