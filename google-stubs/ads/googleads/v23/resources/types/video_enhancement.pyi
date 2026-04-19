from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.video_enhancement_source import (
    VideoEnhancementSourceEnum,
)

_M = TypeVar("_M")

class VideoEnhancement(proto.Message):
    resource_name: str
    duration_millis: int
    source: VideoEnhancementSourceEnum.VideoEnhancementSource
    title: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        duration_millis: int = ...,
        source: VideoEnhancementSourceEnum.VideoEnhancementSource = ...,
        title: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "duration_millis", "source", "title"]
    ) -> bool: ...
