from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.youtube_video_privacy import (
    YouTubeVideoPrivacyEnum,
)
from google.ads.googleads.v23.enums.types.youtube_video_upload_state import (
    YouTubeVideoUploadStateEnum,
)

_M = TypeVar("_M")

class YouTubeVideoUpload(proto.Message):
    resource_name: str
    video_upload_id: int
    channel_id: str
    video_id: str
    state: YouTubeVideoUploadStateEnum.YouTubeVideoUploadState
    video_title: str
    video_description: str
    video_privacy: YouTubeVideoPrivacyEnum.YouTubeVideoPrivacy
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        video_upload_id: int = ...,
        channel_id: str = ...,
        video_id: str = ...,
        state: YouTubeVideoUploadStateEnum.YouTubeVideoUploadState = ...,
        video_title: str = ...,
        video_description: str = ...,
        video_privacy: YouTubeVideoPrivacyEnum.YouTubeVideoPrivacy = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "video_upload_id",
            "channel_id",
            "video_id",
            "state",
            "video_title",
            "video_description",
            "video_privacy",
        ],
    ) -> bool: ...
