from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.access_role import AccessRoleEnum

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
        inviter_user_email_address: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "user_id",
            "email_address",
            "access_role",
            "access_creation_date_time",
            "inviter_user_email_address",
        ],
    ) -> bool: ...
