import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ProductLinkInvitationErrorEnum(proto.Message):
    class ProductLinkInvitationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_STATUS: int
        PERMISSION_DENIED: int
        NO_INVITATION_REQUIRED: int
        CUSTOMER_NOT_PERMITTED_TO_CREATE_INVITATION: int
