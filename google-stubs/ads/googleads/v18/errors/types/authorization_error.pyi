from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AuthorizationErrorEnum(proto.Message):
    class AuthorizationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        USER_PERMISSION_DENIED = 2
        DEVELOPER_TOKEN_NOT_ON_ALLOWLIST = 13
        DEVELOPER_TOKEN_PROHIBITED = 4
        PROJECT_DISABLED = 5
        AUTHORIZATION_ERROR = 6
        ACTION_NOT_PERMITTED = 7
        INCOMPLETE_SIGNUP = 8
        CUSTOMER_NOT_ENABLED = 24
        MISSING_TOS = 9
        DEVELOPER_TOKEN_NOT_APPROVED = 10
        INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION = 11
        SERVICE_ACCESS_DENIED = 12
        ACCESS_DENIED_FOR_ACCOUNT_TYPE = 25
        METRIC_ACCESS_DENIED = 26
        CLOUD_PROJECT_NOT_UNDER_ORGANIZATION = 27
        ACTION_NOT_PERMITTED_FOR_SUSPENDED_ACCOUNT = 28

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
