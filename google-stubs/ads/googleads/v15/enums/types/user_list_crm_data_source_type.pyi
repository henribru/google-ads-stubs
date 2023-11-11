from typing import Any

import proto

class UserListCrmDataSourceTypeEnum(proto.Message):
    class UserListCrmDataSourceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FIRST_PARTY = 2
        THIRD_PARTY_CREDIT_BUREAU = 3
        THIRD_PARTY_VOTER_FILE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
