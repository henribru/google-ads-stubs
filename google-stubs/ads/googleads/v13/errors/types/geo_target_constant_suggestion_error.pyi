from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class GeoTargetConstantSuggestionErrorEnum(proto.Message):
    class GeoTargetConstantSuggestionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOCATION_NAME_SIZE_LIMIT = 2
        LOCATION_NAME_LIMIT = 3
        INVALID_COUNTRY_CODE = 4
        REQUEST_PARAMETERS_UNSET = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
