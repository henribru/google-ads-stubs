from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class GenderTypeEnum(proto.Message):
    class GenderType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MALE = 10
        FEMALE = 11
        UNDETERMINED = 20
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
