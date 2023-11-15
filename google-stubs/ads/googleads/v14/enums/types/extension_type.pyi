from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ExtensionTypeEnum(proto.Message):
    class ExtensionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NONE = 2
        APP = 3
        CALL = 4
        CALLOUT = 5
        MESSAGE = 6
        PRICE = 7
        PROMOTION = 8
        SITELINK = 10
        STRUCTURED_SNIPPET = 11
        LOCATION = 12
        AFFILIATE_LOCATION = 13
        HOTEL_CALLOUT = 15
        IMAGE = 16
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
