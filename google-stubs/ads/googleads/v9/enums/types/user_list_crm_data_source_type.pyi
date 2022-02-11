from typing import Any

import proto

__protobuf__: Any

class UserListCrmDataSourceTypeEnum(proto.Message):
    class UserListCrmDataSourceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FIRST_PARTY: int
        THIRD_PARTY_CREDIT_BUREAU: int
        THIRD_PARTY_VOTER_FILE: int
