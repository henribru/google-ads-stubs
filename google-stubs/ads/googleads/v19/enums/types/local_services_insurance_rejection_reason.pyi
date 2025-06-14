import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesInsuranceRejectionReasonEnum(proto.Message):
    class LocalServicesInsuranceRejectionReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BUSINESS_NAME_MISMATCH: int
        INSURANCE_AMOUNT_INSUFFICIENT: int
        EXPIRED: int
        NO_SIGNATURE: int
        NO_POLICY_NUMBER: int
        NO_COMMERCIAL_GENERAL_LIABILITY: int
        EDITABLE_FORMAT: int
        CATEGORY_MISMATCH: int
        MISSING_EXPIRATION_DATE: int
        POOR_QUALITY: int
        POTENTIALLY_EDITED: int
        WRONG_DOCUMENT_TYPE: int
        NON_FINAL: int
        OTHER: int
