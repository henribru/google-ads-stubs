from typing import Any

import proto

class UserListPrepopulationStatusEnum(proto.Message):
    class UserListPrepopulationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUESTED = 2
        FINISHED = 3
        FAILED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
