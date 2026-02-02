from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AudienceErrorEnum(proto.Message):
    class AudienceError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NAME_ALREADY_IN_USE = 2
        DIMENSION_INVALID = 3
        AUDIENCE_SEGMENT_NOT_FOUND = 4
        AUDIENCE_SEGMENT_TYPE_NOT_SUPPORTED = 5
        DUPLICATE_AUDIENCE_SEGMENT = 6
        TOO_MANY_SEGMENTS = 7
        TOO_MANY_DIMENSIONS_OF_SAME_TYPE = 8
        IN_USE = 9
        MISSING_ASSET_GROUP_ID = 10
        CANNOT_CHANGE_FROM_CUSTOMER_TO_ASSET_GROUP_SCOPE = 11

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
