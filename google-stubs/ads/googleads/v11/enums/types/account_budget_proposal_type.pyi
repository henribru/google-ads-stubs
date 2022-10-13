from typing import Any

import proto

class AccountBudgetProposalTypeEnum(proto.Message):
    class AccountBudgetProposalType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CREATE = 2
        UPDATE = 3
        END = 4
        REMOVE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
