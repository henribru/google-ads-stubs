from typing import Any

import proto

class ProductLinkErrorEnum(proto.Message):
    class ProductLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_OPERATION = 2
        CREATION_NOT_PERMITTED = 3
        INVITATION_EXISTS = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
