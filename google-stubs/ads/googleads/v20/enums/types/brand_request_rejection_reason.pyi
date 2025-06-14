import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BrandRequestRejectionReasonEnum(proto.Message):
    class BrandRequestRejectionReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXISTING_BRAND: int
        EXISTING_BRAND_VARIANT: int
        INCORRECT_INFORMATION: int
        NOT_A_BRAND: int
