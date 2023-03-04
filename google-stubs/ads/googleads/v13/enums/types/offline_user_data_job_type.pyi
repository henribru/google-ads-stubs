from typing import Any

import proto

class OfflineUserDataJobTypeEnum(proto.Message):
    class OfflineUserDataJobType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STORE_SALES_UPLOAD_FIRST_PARTY = 2
        STORE_SALES_UPLOAD_THIRD_PARTY = 3
        CUSTOMER_MATCH_USER_LIST = 4
        CUSTOMER_MATCH_WITH_ATTRIBUTES = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
