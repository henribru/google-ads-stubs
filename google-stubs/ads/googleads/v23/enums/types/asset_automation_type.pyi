import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
        GENERATE_IMAGE_ENHANCEMENT = 7
        GENERATE_IMAGE_EXTRACTION = 9
        GENERATE_DESIGN_VERSIONS_FOR_IMAGES = 10
        FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION = 11
        GENERATE_VIDEOS_FROM_OTHER_ASSETS = 12
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
