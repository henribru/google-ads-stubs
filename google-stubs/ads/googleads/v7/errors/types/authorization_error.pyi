from typing import Any

import proto

__protobuf__: Any

class AuthorizationErrorEnum(proto.Message):
    class AuthorizationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        USER_PERMISSION_DENIED: int
        DEVELOPER_TOKEN_NOT_ON_ALLOWLIST: int
        DEVELOPER_TOKEN_PROHIBITED: int
        PROJECT_DISABLED: int
        AUTHORIZATION_ERROR: int
        ACTION_NOT_PERMITTED: int
        INCOMPLETE_SIGNUP: int
        CUSTOMER_NOT_ENABLED: int
        MISSING_TOS: int
        DEVELOPER_TOKEN_NOT_APPROVED: int
        INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION: int
        SERVICE_ACCESS_DENIED: int
        ACCESS_DENIED_FOR_ACCOUNT_TYPE: int
