import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccountBudgetProposalTypeEnum(proto.Message):
    class AccountBudgetProposalType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CREATE: int
        UPDATE: int
        END: int
        REMOVE: int
