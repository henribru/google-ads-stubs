from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class UserListCustomerTypeErrorEnum(proto.Message):
    class UserListCustomerTypeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONFLICTING_CUSTOMER_TYPES = 2
        NO_ACCESS_TO_USER_LIST = 3
        USERLIST_NOT_ELIGIBLE = 4
        CONVERSION_TRACKING_NOT_ENABLED_OR_NOT_MCC_MANAGER_ACCOUNT = 5
        TOO_MANY_USER_LISTS_FOR_THE_CUSTOMER_TYPE = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
