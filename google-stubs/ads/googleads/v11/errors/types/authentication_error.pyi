from typing import Any

import proto

class AuthenticationErrorEnum(proto.Message):
    class AuthenticationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AUTHENTICATION_ERROR = 2
        CLIENT_CUSTOMER_ID_INVALID = 5
        CUSTOMER_NOT_FOUND = 8
        GOOGLE_ACCOUNT_DELETED = 9
        GOOGLE_ACCOUNT_COOKIE_INVALID = 10
        GOOGLE_ACCOUNT_AUTHENTICATION_FAILED = 25
        GOOGLE_ACCOUNT_USER_AND_ADS_USER_MISMATCH = 12
        LOGIN_COOKIE_REQUIRED = 13
        NOT_ADS_USER = 14
        OAUTH_TOKEN_INVALID = 15
        OAUTH_TOKEN_EXPIRED = 16
        OAUTH_TOKEN_DISABLED = 17
        OAUTH_TOKEN_REVOKED = 18
        OAUTH_TOKEN_HEADER_INVALID = 19
        LOGIN_COOKIE_INVALID = 20
        USER_ID_INVALID = 22
        TWO_STEP_VERIFICATION_NOT_ENROLLED = 23
        ADVANCED_PROTECTION_NOT_ENROLLED = 24
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
