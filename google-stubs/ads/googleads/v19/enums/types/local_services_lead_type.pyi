import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLeadTypeEnum(proto.Message):
    class LeadType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MESSAGE: int
        PHONE_CALL: int
        BOOKING: int
