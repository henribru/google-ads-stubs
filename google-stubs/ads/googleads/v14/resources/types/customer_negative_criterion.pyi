from typing import Any

import proto

from google.ads.googleads.v14.common.types.criteria import (
    ContentLabelInfo,
    MobileAppCategoryInfo,
    MobileApplicationInfo,
    NegativeKeywordListInfo,
    PlacementInfo,
    YouTubeChannelInfo,
    YouTubeVideoInfo,
)
from google.ads.googleads.v14.enums.types.criterion_type import CriterionTypeEnum

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        type_: CriterionTypeEnum.CriterionType = ...,
        content_label: ContentLabelInfo = ...,
        mobile_application: MobileApplicationInfo = ...,
        mobile_app_category: MobileAppCategoryInfo = ...,
        placement: PlacementInfo = ...,
        youtube_video: YouTubeVideoInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        negative_keyword_list: NegativeKeywordListInfo = ...
    ) -> None: ...
