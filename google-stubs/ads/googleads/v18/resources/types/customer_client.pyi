import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import customer_status
from typing import MutableSequence

__protobuf__: Incomplete

class CustomerClient(proto.Message):
    resource_name: str
    client_customer: str
    hidden: bool
    level: int
    time_zone: str
    test_account: bool
    manager: bool
    descriptive_name: str
    currency_code: str
    id: int
    applied_labels: MutableSequence[str]
    status: customer_status.CustomerStatusEnum.CustomerStatus
