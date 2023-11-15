from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.access_role import AccessRoleEnum

_M = TypeVar("_M")

class CustomerUserAccess(proto.Message):
    resource_name: str
    user_id: int
    email_address: str
    access_role: AccessRoleEnum.AccessRole
    access_creation_date_time: str
    inviter_user_email_address: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        user_id: int = ...,
        email_address: str = ...,
        access_role: AccessRoleEnum.AccessRole = ...,
        access_creation_date_time: str = ...,
        inviter_user_email_address: str = ...
    ) -> None: ...
