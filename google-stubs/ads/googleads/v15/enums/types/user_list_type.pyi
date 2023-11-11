from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class UserListTypeEnum(proto.Message):
    class UserListType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REMARKETING = 2
        LOGICAL = 3
        EXTERNAL_REMARKETING = 4
        RULE_BASED = 5
        SIMILAR = 6
        CRM_BASED = 7
        LOOKALIKE = 9
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
