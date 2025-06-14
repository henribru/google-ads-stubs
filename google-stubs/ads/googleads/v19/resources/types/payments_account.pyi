import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PaymentsAccount(proto.Message):
    resource_name: str
    payments_account_id: str
    name: str
    currency_code: str
    payments_profile_id: str
    secondary_payments_profile_id: str
    paying_manager_customer: str
