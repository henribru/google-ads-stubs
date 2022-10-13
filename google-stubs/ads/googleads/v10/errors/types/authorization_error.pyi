from typing import Any

import proto

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
