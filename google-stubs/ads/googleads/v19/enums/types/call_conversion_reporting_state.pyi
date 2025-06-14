import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CallConversionReportingStateEnum(proto.Message):
    class CallConversionReportingState(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DISABLED: int
        USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION: int
        USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION: int
