from typing import Any

import proto

class ManagerLinkErrorEnum(proto.Message):
    class ManagerLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING = 2
        TOO_MANY_MANAGERS = 3
        TOO_MANY_INVITES = 4
        ALREADY_INVITED_BY_THIS_MANAGER = 5
        ALREADY_MANAGED_BY_THIS_MANAGER = 6
        ALREADY_MANAGED_IN_HIERARCHY = 7
        DUPLICATE_CHILD_FOUND = 8
        CLIENT_HAS_NO_ADMIN_USER = 9
        MAX_DEPTH_EXCEEDED = 10
        CYCLE_NOT_ALLOWED = 11
        TOO_MANY_ACCOUNTS = 12
        TOO_MANY_ACCOUNTS_AT_MANAGER = 13
        NON_OWNER_USER_CANNOT_MODIFY_LINK = 14
        SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS = 15
        CLIENT_OUTSIDE_TREE = 16
        INVALID_STATUS_CHANGE = 17
        INVALID_CHANGE = 18
        CUSTOMER_CANNOT_MANAGE_SELF = 19
        CREATING_ENABLED_LINK_NOT_ALLOWED = 20
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
