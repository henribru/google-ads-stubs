from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.customer_status import CustomerStatusEnum

_M = TypeVar("_M")

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
    status: CustomerStatusEnum.CustomerStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
        applied_labels: MutableSequence[str] = ...,
        status: CustomerStatusEnum.CustomerStatus = ...
    ) -> None: ...
