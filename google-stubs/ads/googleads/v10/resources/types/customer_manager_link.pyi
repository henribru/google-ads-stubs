from typing import Any

import proto

from google.ads.googleads.v10.enums.types.manager_link_status import (
    ManagerLinkStatusEnum,
)

class CustomerManagerLink(proto.Message):
    resource_name: str
    manager_customer: str
    manager_link_id: int
    status: ManagerLinkStatusEnum.ManagerLinkStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        manager_customer: str = ...,
        manager_link_id: int = ...,
        status: ManagerLinkStatusEnum.ManagerLinkStatus = ...
    ) -> None: ...
