from typing import Any

import proto

__protobuf__: Any

class AuthenticationErrorEnum(proto.Message):
    class AuthenticationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AUTHENTICATION_ERROR: int
        CLIENT_CUSTOMER_ID_INVALID: int
        CUSTOMER_NOT_FOUND: int
        GOOGLE_ACCOUNT_DELETED: int
        GOOGLE_ACCOUNT_COOKIE_INVALID: int
        GOOGLE_ACCOUNT_AUTHENTICATION_FAILED: int
        GOOGLE_ACCOUNT_USER_AND_ADS_USER_MISMATCH: int
        LOGIN_COOKIE_REQUIRED: int
        NOT_ADS_USER: int
        OAUTH_TOKEN_INVALID: int
        OAUTH_TOKEN_EXPIRED: int
        OAUTH_TOKEN_DISABLED: int
        OAUTH_TOKEN_REVOKED: int
        OAUTH_TOKEN_HEADER_INVALID: int
        LOGIN_COOKIE_INVALID: int
        USER_ID_INVALID: int
        TWO_STEP_VERIFICATION_NOT_ENROLLED: int
        ADVANCED_PROTECTION_NOT_ENROLLED: int
