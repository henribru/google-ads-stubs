from typing import Any

import proto

from google.ads.googleads.v11.common.types.criteria import (
    KeywordInfo,
    MobileAppCategoryInfo,
    MobileApplicationInfo,
    PlacementInfo,
    YouTubeChannelInfo,
    YouTubeVideoInfo,
)
from google.ads.googleads.v11.enums.types.criterion_type import CriterionTypeEnum

class SharedCriterion(proto.Message):
    resource_name: str
    shared_set: str
    criterion_id: int
    type_: CriterionTypeEnum.CriterionType
    keyword: KeywordInfo
    youtube_video: YouTubeVideoInfo
    youtube_channel: YouTubeChannelInfo
    placement: PlacementInfo
    mobile_app_category: MobileAppCategoryInfo
    mobile_application: MobileApplicationInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        shared_set: str = ...,
        criterion_id: int = ...,
        type_: CriterionTypeEnum.CriterionType = ...,
        keyword: KeywordInfo = ...,
        youtube_video: YouTubeVideoInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        placement: PlacementInfo = ...,
        mobile_app_category: MobileAppCategoryInfo = ...,
        mobile_application: MobileApplicationInfo = ...
    ) -> None: ...
