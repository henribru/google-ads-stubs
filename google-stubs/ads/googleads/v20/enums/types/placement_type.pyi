from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PlacementTypeEnum(proto.Message):
    class PlacementType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WEBSITE = 2
        MOBILE_APP_CATEGORY = 3
        MOBILE_APPLICATION = 4
        YOUTUBE_VIDEO = 5
        YOUTUBE_CHANNEL = 6
        GOOGLE_PRODUCTS = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
