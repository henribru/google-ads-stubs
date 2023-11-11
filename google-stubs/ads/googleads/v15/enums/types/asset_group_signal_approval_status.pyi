from typing import Any

import proto

class AssetGroupSignalApprovalStatusEnum(proto.Message):
    class AssetGroupSignalApprovalStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPROVED = 2
        LIMITED = 3
        DISAPPROVED = 4
        UNDER_REVIEW = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
