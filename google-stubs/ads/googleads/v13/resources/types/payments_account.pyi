from typing import Any

import proto

class PaymentsAccount(proto.Message):
    resource_name: str
    payments_account_id: str
    name: str
    currency_code: str
    payments_profile_id: str
    secondary_payments_profile_id: str
    paying_manager_customer: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        payments_account_id: str = ...,
        name: str = ...,
        currency_code: str = ...,
        payments_profile_id: str = ...,
        secondary_payments_profile_id: str = ...,
        paying_manager_customer: str = ...
    ) -> None: ...
