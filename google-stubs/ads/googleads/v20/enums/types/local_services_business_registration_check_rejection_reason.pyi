import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesBusinessRegistrationCheckRejectionReasonEnum(proto.Message):
    class LocalServicesBusinessRegistrationCheckRejectionReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BUSINESS_NAME_MISMATCH: int
        BUSINESS_DETAILS_MISMATCH: int
        ID_NOT_FOUND: int
        POOR_DOCUMENT_IMAGE_QUALITY: int
        DOCUMENT_EXPIRED: int
        DOCUMENT_INVALID: int
        DOCUMENT_TYPE_MISMATCH: int
        DOCUMENT_UNVERIFIABLE: int
        OTHER: int
