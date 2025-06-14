import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLicenseRejectionReasonEnum(proto.Message):
    class LocalServicesLicenseRejectionReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BUSINESS_NAME_MISMATCH: int
        UNAUTHORIZED: int
        EXPIRED: int
        POOR_QUALITY: int
        UNVERIFIABLE: int
        WRONG_DOCUMENT_OR_ID: int
        OTHER: int
