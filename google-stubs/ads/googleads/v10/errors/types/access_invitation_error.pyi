import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccessInvitationErrorEnum(proto.Message):
    class AccessInvitationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_EMAIL_ADDRESS: int
        EMAIL_ADDRESS_ALREADY_HAS_ACCESS: int
        INVALID_INVITATION_STATUS: int
        GOOGLE_CONSUMER_ACCOUNT_NOT_ALLOWED: int
        INVALID_INVITATION_ID: int
        EMAIL_ADDRESS_ALREADY_HAS_PENDING_INVITATION: int
        PENDING_INVITATIONS_LIMIT_EXCEEDED: int
        EMAIL_DOMAIN_POLICY_VIOLATED: int
