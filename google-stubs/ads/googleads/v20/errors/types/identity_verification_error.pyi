import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class IdentityVerificationErrorEnum(proto.Message):
    class IdentityVerificationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NO_EFFECTIVE_BILLING: int
        BILLING_NOT_ON_MONTHLY_INVOICING: int
        VERIFICATION_ALREADY_STARTED: int
