from typing import Any

import proto

__protobuf__: Any

class OfflineUserDataJobTypeEnum(proto.Message):
    class OfflineUserDataJobType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STORE_SALES_UPLOAD_FIRST_PARTY: int
        STORE_SALES_UPLOAD_THIRD_PARTY: int
        CUSTOMER_MATCH_USER_LIST: int
        CUSTOMER_MATCH_WITH_ATTRIBUTES: int
