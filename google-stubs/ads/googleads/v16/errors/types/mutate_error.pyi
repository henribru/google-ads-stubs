from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class MutateErrorEnum(proto.Message):
    class MutateError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESOURCE_NOT_FOUND = 3
        ID_EXISTS_IN_MULTIPLE_MUTATES = 7
        INCONSISTENT_FIELD_VALUES = 8
        MUTATE_NOT_ALLOWED = 9
        RESOURCE_NOT_IN_GOOGLE_ADS = 10
        RESOURCE_ALREADY_EXISTS = 11
        RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY = 12
        OPERATION_DOES_NOT_SUPPORT_PARTIAL_FAILURE = 16
        RESOURCE_READ_ONLY = 13

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
