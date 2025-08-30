from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v21.common.types.criteria import (
    ContentLabelInfo,
    IpBlockInfo,
    MobileAppCategoryInfo,
    MobileApplicationInfo,
    NegativeKeywordListInfo,
    PlacementInfo,
    PlacementListInfo,
    YouTubeChannelInfo,
    YouTubeVideoInfo,
)
from google.ads.googleads.v21.enums.types.criterion_type import CriterionTypeEnum

_M = TypeVar("_M")

class CustomerNegativeCriterion(proto.Message):
    resource_name: str
    id: int
    type_: CriterionTypeEnum.CriterionType
    content_label: ContentLabelInfo
    mobile_application: MobileApplicationInfo
    mobile_app_category: MobileAppCategoryInfo
    placement: PlacementInfo
    youtube_video: YouTubeVideoInfo
    youtube_channel: YouTubeChannelInfo
    negative_keyword_list: NegativeKeywordListInfo
    ip_block: IpBlockInfo
    placement_list: PlacementListInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        type_: CriterionTypeEnum.CriterionType = ...,
        content_label: ContentLabelInfo = ...,
        mobile_application: MobileApplicationInfo = ...,
        mobile_app_category: MobileAppCategoryInfo = ...,
        placement: PlacementInfo = ...,
        youtube_video: YouTubeVideoInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        negative_keyword_list: NegativeKeywordListInfo = ...,
        ip_block: IpBlockInfo = ...,
        placement_list: PlacementListInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "type_",
            "content_label",
            "mobile_application",
            "mobile_app_category",
            "placement",
            "youtube_video",
            "youtube_channel",
            "negative_keyword_list",
            "ip_block",
            "placement_list",
        ],
    ) -> bool: ...
