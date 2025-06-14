import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomerAcquisitionOptimizationModeEnum(proto.Message):
    class CustomerAcquisitionOptimizationMode(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TARGET_ALL_EQUALLY: int
        BID_HIGHER_FOR_NEW_CUSTOMER: int
        TARGET_NEW_CUSTOMER: int
