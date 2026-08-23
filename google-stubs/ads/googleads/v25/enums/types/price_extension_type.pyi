from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PriceExtensionTypeEnum(proto.Message):
    class PriceExtensionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BRANDS = 2
        EVENTS = 3
        LOCATIONS = 4
        NEIGHBORHOODS = 5
        PRODUCT_CATEGORIES = 6
        PRODUCT_TIERS = 7
        SERVICES = 8
        SERVICE_CATEGORIES = 9
        SERVICE_TIERS = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
