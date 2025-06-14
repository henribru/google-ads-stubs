import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListCrmDataSourceTypeEnum(proto.Message):
    class UserListCrmDataSourceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FIRST_PARTY: int
        THIRD_PARTY_CREDIT_BUREAU: int
        THIRD_PARTY_VOTER_FILE: int
