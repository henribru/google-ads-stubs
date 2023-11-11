from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.manager_link_status import (
    ManagerLinkStatusEnum,
)

_M = TypeVar("_M")

class CustomerManagerLink(proto.Message):
    resource_name: str
    manager_customer: str
    manager_link_id: int
    status: ManagerLinkStatusEnum.ManagerLinkStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        manager_customer: str = ...,
        manager_link_id: int = ...,
        status: ManagerLinkStatusEnum.ManagerLinkStatus = ...
    ) -> None: ...
