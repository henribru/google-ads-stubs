from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v21.enums.types.data_link_status import DataLinkStatusEnum
from google.ads.googleads.v21.enums.types.data_link_type import DataLinkTypeEnum

_M = TypeVar("_M")

class DataLink(proto.Message):
    resource_name: str
    product_link_id: int
    data_link_id: int
    type_: DataLinkTypeEnum.DataLinkType
    status: DataLinkStatusEnum.DataLinkStatus
    youtube_video: YoutubeVideoIdentifier
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        product_link_id: int = ...,
        data_link_id: int = ...,
        type_: DataLinkTypeEnum.DataLinkType = ...,
        status: DataLinkStatusEnum.DataLinkStatus = ...,
        youtube_video: YoutubeVideoIdentifier = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "product_link_id",
            "data_link_id",
            "type_",
            "status",
            "youtube_video",
        ],
    ) -> bool: ...

class YoutubeVideoIdentifier(proto.Message):
    channel_id: str
    video_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        channel_id: str = ...,
        video_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["channel_id", "video_id"]
    ) -> bool: ...
