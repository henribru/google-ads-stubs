from typing import Any

import proto

__protobuf__: Any

class ProductBiddingCategoryStatusEnum(proto.Message):
    class ProductBiddingCategoryStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACTIVE: int
        OBSOLETE: int
