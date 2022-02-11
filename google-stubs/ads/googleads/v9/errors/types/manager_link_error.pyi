from typing import Any

import proto

__protobuf__: Any

class ManagerLinkErrorEnum(proto.Message):
    class ManagerLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING: int
        TOO_MANY_MANAGERS: int
        TOO_MANY_INVITES: int
        ALREADY_INVITED_BY_THIS_MANAGER: int
        ALREADY_MANAGED_BY_THIS_MANAGER: int
        ALREADY_MANAGED_IN_HIERARCHY: int
        DUPLICATE_CHILD_FOUND: int
        CLIENT_HAS_NO_ADMIN_USER: int
        MAX_DEPTH_EXCEEDED: int
        CYCLE_NOT_ALLOWED: int
        TOO_MANY_ACCOUNTS: int
        TOO_MANY_ACCOUNTS_AT_MANAGER: int
        NON_OWNER_USER_CANNOT_MODIFY_LINK: int
        SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS: int
        CLIENT_OUTSIDE_TREE: int
        INVALID_STATUS_CHANGE: int
        INVALID_CHANGE: int
        CUSTOMER_CANNOT_MANAGE_SELF: int
        CREATING_ENABLED_LINK_NOT_ALLOWED: int
