from typing import Any

import proto

__protobuf__: Any

class CustomerManagerLinkErrorEnum(proto.Message):
    class CustomerManagerLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NO_PENDING_INVITE: int
        SAME_CLIENT_MORE_THAN_ONCE_PER_CALL: int
        MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS: int
        CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER: int
        CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER: int
        CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER: int
        CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT: int
        DUPLICATE_CHILD_FOUND: int
        TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS: int
