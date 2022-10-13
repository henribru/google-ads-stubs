from typing import Any

import proto

class AccessInvitationErrorEnum(proto.Message):
    class AccessInvitationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_EMAIL_ADDRESS = 2
        EMAIL_ADDRESS_ALREADY_HAS_ACCESS = 3
        INVALID_INVITATION_STATUS = 4
        GOOGLE_CONSUMER_ACCOUNT_NOT_ALLOWED = 5
        INVALID_INVITATION_ID = 6
        EMAIL_ADDRESS_ALREADY_HAS_PENDING_INVITATION = 7
        PENDING_INVITATIONS_LIMIT_EXCEEDED = 8
        EMAIL_DOMAIN_POLICY_VIOLATED = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
