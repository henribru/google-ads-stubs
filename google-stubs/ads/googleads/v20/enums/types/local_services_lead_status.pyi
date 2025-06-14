import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLeadStatusEnum(proto.Message):
    class LeadStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEW: int
        ACTIVE: int
        BOOKED: int
        DECLINED: int
        EXPIRED: int
        DISABLED: int
        CONSUMER_DECLINED: int
        WIPED_OUT: int
