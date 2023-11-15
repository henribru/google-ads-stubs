from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.criteria import (
    BrandInfo,
    KeywordInfo,
    MobileAppCategoryInfo,
    MobileApplicationInfo,
    PlacementInfo,
    YouTubeChannelInfo,
    YouTubeVideoInfo,
)
from google.ads.googleads.v15.enums.types.criterion_type import CriterionTypeEnum

_M = TypeVar("_M")

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
    brand: BrandInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        shared_set: str = ...,
        criterion_id: int = ...,
        type_: CriterionTypeEnum.CriterionType = ...,
        keyword: KeywordInfo = ...,
        youtube_video: YouTubeVideoInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        placement: PlacementInfo = ...,
        mobile_app_category: MobileAppCategoryInfo = ...,
        mobile_application: MobileApplicationInfo = ...,
        brand: BrandInfo = ...
    ) -> None: ...
