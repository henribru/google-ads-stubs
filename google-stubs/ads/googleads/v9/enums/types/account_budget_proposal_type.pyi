from typing import Any

import proto

__protobuf__: Any

class AccountBudgetProposalTypeEnum(proto.Message):
    class AccountBudgetProposalType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CREATE: int
        UPDATE: int
        END: int
        REMOVE: int
