from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    billing_setup_status as billing_setup_status,
    time_type as time_type,
)

__protobuf__: Any

class BillingSetup(proto.Message):
    class PaymentsAccountInfo(proto.Message):
        payments_account_id: Any
        payments_account_name: Any
        payments_profile_id: Any
        payments_profile_name: Any
        secondary_payments_profile_id: Any
    resource_name: Any
    id: Any
    status: Any
    payments_account: Any
    payments_account_info: Any
    start_date_time: Any
    start_time_type: Any
    end_date_time: Any
    end_time_type: Any
