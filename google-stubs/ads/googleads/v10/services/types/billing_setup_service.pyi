from typing import Any

import proto

from google.ads.googleads.v10.resources.types.billing_setup import BillingSetup

class BillingSetupOperation(proto.Message):
    create: BillingSetup
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: BillingSetup = ...,
        remove: str = ...
    ) -> None: ...

class MutateBillingSetupRequest(proto.Message):
    customer_id: str
    operation: BillingSetupOperation
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: BillingSetupOperation = ...
    ) -> None: ...

class MutateBillingSetupResponse(proto.Message):
    result: MutateBillingSetupResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateBillingSetupResult = ...
    ) -> None: ...

class MutateBillingSetupResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
