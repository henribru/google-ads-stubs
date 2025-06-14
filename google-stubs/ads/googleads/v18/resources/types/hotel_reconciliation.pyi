import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import hotel_reconciliation_status

__protobuf__: Incomplete

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
    status: hotel_reconciliation_status.HotelReconciliationStatusEnum.HotelReconciliationStatus
