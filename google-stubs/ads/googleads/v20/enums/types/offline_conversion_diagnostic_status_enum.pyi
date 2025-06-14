import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class OfflineConversionDiagnosticStatusEnum(proto.Message):
    class OfflineConversionDiagnosticStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXCELLENT: int
        GOOD: int
        NEEDS_ATTENTION: int
        NO_RECENT_UPLOAD: int
