from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
