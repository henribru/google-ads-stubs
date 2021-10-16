from typing import Any

import proto

__protobuf__: Any

class CustomerClientLinkErrorEnum(proto.Message):
    class CustomerClientLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CLIENT_ALREADY_INVITED_BY_THIS_MANAGER: int
        CLIENT_ALREADY_MANAGED_IN_HIERARCHY: int
        CYCLIC_LINK_NOT_ALLOWED: int
        CUSTOMER_HAS_TOO_MANY_ACCOUNTS: int
        CLIENT_HAS_TOO_MANY_INVITATIONS: int
        CANNOT_HIDE_OR_UNHIDE_MANAGER_ACCOUNTS: int
        CUSTOMER_HAS_TOO_MANY_ACCOUNTS_AT_MANAGER: int
        CLIENT_HAS_TOO_MANY_MANAGERS: int
