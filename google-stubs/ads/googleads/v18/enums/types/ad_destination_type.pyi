from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdDestinationTypeEnum(proto.Message):
    class AdDestinationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_APPLICABLE = 2
        WEBSITE = 3
        APP_DEEP_LINK = 4
        APP_STORE = 5
        PHONE_CALL = 6
        MAP_DIRECTIONS = 7
        LOCATION_LISTING = 8
        MESSAGE = 9
        LEAD_FORM = 10
        YOUTUBE = 11
        UNMODELED_FOR_CONVERSIONS = 12

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
