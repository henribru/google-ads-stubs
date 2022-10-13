from typing import Any

import proto

from google.ads.googleads.v11.enums.types.customer_status import CustomerStatusEnum

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
    applied_labels: list[str]
    status: CustomerStatusEnum.CustomerStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        client_customer: str = ...,
        hidden: bool = ...,
        level: int = ...,
        time_zone: str = ...,
        test_account: bool = ...,
        manager: bool = ...,
        descriptive_name: str = ...,
        currency_code: str = ...,
        id: int = ...,
        applied_labels: list[str] = ...,
        status: CustomerStatusEnum.CustomerStatus = ...
    ) -> None: ...
