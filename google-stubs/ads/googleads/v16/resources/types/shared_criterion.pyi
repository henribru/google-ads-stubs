from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.criteria import (
    BrandInfo,
    KeywordInfo,
    MobileAppCategoryInfo,
    MobileApplicationInfo,
    PlacementInfo,
    YouTubeChannelInfo,
    YouTubeVideoInfo,
)
from google.ads.googleads.v16.enums.types.criterion_type import CriterionTypeEnum

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
        brand: BrandInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "shared_set",
            "criterion_id",
            "type_",
            "keyword",
            "youtube_video",
            "youtube_channel",
            "placement",
            "mobile_app_category",
            "mobile_application",
            "brand",
        ],
    ) -> bool: ...
