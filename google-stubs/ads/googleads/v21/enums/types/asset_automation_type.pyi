from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetAutomationTypeEnum(proto.Message):
    class AssetAutomationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT_ASSET_AUTOMATION = 2
        GENERATE_VERTICAL_YOUTUBE_VIDEOS = 3
        GENERATE_SHORTER_YOUTUBE_VIDEOS = 4
        GENERATE_LANDING_PAGE_PREVIEW = 5
        GENERATE_ENHANCED_YOUTUBE_VIDEOS = 6
        FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION = 11

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
