from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class OfflineUserDataJobTypeEnum(proto.Message):
    class OfflineUserDataJobType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STORE_SALES_UPLOAD_FIRST_PARTY = 2
        STORE_SALES_UPLOAD_THIRD_PARTY = 3
        CUSTOMER_MATCH_USER_LIST = 4
        CUSTOMER_MATCH_WITH_ATTRIBUTES = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
