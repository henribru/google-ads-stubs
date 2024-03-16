from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.manager_link_status import (
    ManagerLinkStatusEnum,
)

_M = TypeVar("_M")

class CustomerClientLink(proto.Message):
    resource_name: str
    client_customer: str
    manager_link_id: int
    status: ManagerLinkStatusEnum.ManagerLinkStatus
    hidden: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        client_customer: str = ...,
        manager_link_id: int = ...,
        status: ManagerLinkStatusEnum.ManagerLinkStatus = ...,
        hidden: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "client_customer", "manager_link_id", "status", "hidden"
        ],
    ) -> bool: ...
