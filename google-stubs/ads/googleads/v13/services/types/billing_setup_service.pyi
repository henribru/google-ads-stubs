from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.resources.types.billing_setup import BillingSetup

_M = TypeVar("_M")

class BillingSetupOperation(proto.Message):
    create: BillingSetup
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: BillingSetup = ...,
        remove: str = ...
    ) -> None: ...

class MutateBillingSetupRequest(proto.Message):
    customer_id: str
    operation: BillingSetupOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: BillingSetupOperation = ...
    ) -> None: ...

class MutateBillingSetupResponse(proto.Message):
    result: MutateBillingSetupResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateBillingSetupResult = ...
    ) -> None: ...

class MutateBillingSetupResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
