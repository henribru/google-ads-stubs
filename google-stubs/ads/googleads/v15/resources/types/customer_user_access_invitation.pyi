from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.access_invitation_status import (
    AccessInvitationStatusEnum,
)
from google.ads.googleads.v15.enums.types.access_role import AccessRoleEnum

_M = TypeVar("_M")

class CustomerUserAccessInvitation(proto.Message):
    resource_name: str
    invitation_id: int
    access_role: AccessRoleEnum.AccessRole
    email_address: str
    creation_date_time: str
    invitation_status: AccessInvitationStatusEnum.AccessInvitationStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        invitation_id: int = ...,
        access_role: AccessRoleEnum.AccessRole = ...,
        email_address: str = ...,
        creation_date_time: str = ...,
        invitation_status: AccessInvitationStatusEnum.AccessInvitationStatus = ...
    ) -> None: ...
