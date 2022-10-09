import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PolicyFindingErrorEnum(proto.Message):
    class PolicyFindingError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        POLICY_FINDING: int
        POLICY_TOPIC_NOT_FOUND: int
