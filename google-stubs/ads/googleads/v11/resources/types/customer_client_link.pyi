from typing import Any

import proto

from google.ads.googleads.v11.enums.types.manager_link_status import (
    ManagerLinkStatusEnum,
)

class CustomerClientLink(proto.Message):
    resource_name: str
    client_customer: str
    manager_link_id: int
    status: ManagerLinkStatusEnum.ManagerLinkStatus
    hidden: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        client_customer: str = ...,
        manager_link_id: int = ...,
        status: ManagerLinkStatusEnum.ManagerLinkStatus = ...,
        hidden: bool = ...
    ) -> None: ...
