import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    billing_setup_status as billing_setup_status,
    time_type as time_type,
)

__protobuf__: Incomplete

class BillingSetup(proto.Message):
    class PaymentsAccountInfo(proto.Message):
        payments_account_id: Incomplete
        payments_account_name: Incomplete
        payments_profile_id: Incomplete
        payments_profile_name: Incomplete
        secondary_payments_profile_id: Incomplete
    resource_name: Incomplete
    id: Incomplete
    status: Incomplete
    payments_account: Incomplete
    payments_account_info: Incomplete
    start_date_time: Incomplete
    start_time_type: Incomplete
    end_date_time: Incomplete
    end_time_type: Incomplete
