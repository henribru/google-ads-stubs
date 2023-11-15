from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CustomAudienceTypeEnum(proto.Message):
    class CustomAudienceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AUTO = 2
        INTEREST = 3
        PURCHASE_INTENT = 4
        SEARCH = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
