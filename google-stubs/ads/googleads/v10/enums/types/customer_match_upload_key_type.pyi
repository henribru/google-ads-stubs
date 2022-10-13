from typing import Any

import proto

class CustomerMatchUploadKeyTypeEnum(proto.Message):
    class CustomerMatchUploadKeyType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONTACT_INFO = 2
        CRM_ID = 3
        MOBILE_ADVERTISING_ID = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
