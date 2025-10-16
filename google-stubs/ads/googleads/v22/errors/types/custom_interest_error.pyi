from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomInterestErrorEnum(proto.Message):
    class CustomInterestError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NAME_ALREADY_USED = 2
        CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE = 3
        TYPE_AND_PARAMETER_NOT_FOUND = 4
        TYPE_AND_PARAMETER_ALREADY_EXISTED = 5
        INVALID_CUSTOM_INTEREST_MEMBER_TYPE = 6
        CANNOT_REMOVE_WHILE_IN_USE = 7
        CANNOT_CHANGE_TYPE = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
