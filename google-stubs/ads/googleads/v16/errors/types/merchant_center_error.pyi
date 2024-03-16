from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class MerchantCenterErrorEnum(proto.Message):
    class MerchantCenterError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MERCHANT_ID_CANNOT_BE_ACCESSED = 2
        CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX = 3

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
