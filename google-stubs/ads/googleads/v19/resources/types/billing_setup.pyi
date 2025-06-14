import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import billing_setup_status, time_type

__protobuf__: Incomplete

class BillingSetup(proto.Message):
    class PaymentsAccountInfo(proto.Message):
        payments_account_id: str
        payments_account_name: str
        payments_profile_id: str
        payments_profile_name: str
        secondary_payments_profile_id: str
    resource_name: str
    id: int
    status: billing_setup_status.BillingSetupStatusEnum.BillingSetupStatus
    payments_account: str
    payments_account_info: PaymentsAccountInfo
    start_date_time: str
    start_time_type: time_type.TimeTypeEnum.TimeType
    end_date_time: str
    end_time_type: time_type.TimeTypeEnum.TimeType
