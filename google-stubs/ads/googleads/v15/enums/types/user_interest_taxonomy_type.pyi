from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class UserInterestTaxonomyTypeEnum(proto.Message):
    class UserInterestTaxonomyType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AFFINITY = 2
        IN_MARKET = 3
        MOBILE_APP_INSTALL_USER = 4
        VERTICAL_GEO = 5
        NEW_SMART_PHONE_USER = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
