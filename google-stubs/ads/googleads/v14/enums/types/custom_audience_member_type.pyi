from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CustomAudienceMemberTypeEnum(proto.Message):
    class CustomAudienceMemberType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        KEYWORD = 2
        URL = 3
        PLACE_CATEGORY = 4
        APP = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
