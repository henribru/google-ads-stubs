from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomerManagerLinkErrorEnum(proto.Message):
    class CustomerManagerLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_PENDING_INVITE = 2
        SAME_CLIENT_MORE_THAN_ONCE_PER_CALL = 3
        MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS = 4
        CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER = 5
        CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER = 6
        CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER = 7
        CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT = 8
        DUPLICATE_CHILD_FOUND = 9
        TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
