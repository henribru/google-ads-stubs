from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class HotelAssetSuggestionStatusEnum(proto.Message):
    class HotelAssetSuggestionStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SUCCESS = 2
        HOTEL_NOT_FOUND = 3
        INVALID_PLACE_ID = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
