from typing import Any

import proto

class CustomerClientLinkErrorEnum(proto.Message):
    class CustomerClientLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLIENT_ALREADY_INVITED_BY_THIS_MANAGER = 2
        CLIENT_ALREADY_MANAGED_IN_HIERARCHY = 3
        CYCLIC_LINK_NOT_ALLOWED = 4
        CUSTOMER_HAS_TOO_MANY_ACCOUNTS = 5
        CLIENT_HAS_TOO_MANY_INVITATIONS = 6
        CANNOT_HIDE_OR_UNHIDE_MANAGER_ACCOUNTS = 7
        CUSTOMER_HAS_TOO_MANY_ACCOUNTS_AT_MANAGER = 8
        CLIENT_HAS_TOO_MANY_MANAGERS = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
