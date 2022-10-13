from typing import Any

import proto

from google.ads.googleads.v10.enums.types.access_invitation_status import (
    AccessInvitationStatusEnum,
)
from google.ads.googleads.v10.enums.types.access_role import AccessRoleEnum

class CustomerUserAccessInvitation(proto.Message):
    resource_name: str
    invitation_id: int
    access_role: AccessRoleEnum.AccessRole
    email_address: str
    creation_date_time: str
    invitation_status: AccessInvitationStatusEnum.AccessInvitationStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        invitation_id: int = ...,
        access_role: AccessRoleEnum.AccessRole = ...,
        email_address: str = ...,
        creation_date_time: str = ...,
        invitation_status: AccessInvitationStatusEnum.AccessInvitationStatus = ...
    ) -> None: ...
