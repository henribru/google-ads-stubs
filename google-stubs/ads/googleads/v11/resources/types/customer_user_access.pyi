from typing import Any

import proto

from google.ads.googleads.v11.enums.types.access_role import AccessRoleEnum

class CustomerUserAccess(proto.Message):
    resource_name: str
    user_id: int
    email_address: str
    access_role: AccessRoleEnum.AccessRole
    access_creation_date_time: str
    inviter_user_email_address: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        user_id: int = ...,
        email_address: str = ...,
        access_role: AccessRoleEnum.AccessRole = ...,
        access_creation_date_time: str = ...,
        inviter_user_email_address: str = ...
    ) -> None: ...
