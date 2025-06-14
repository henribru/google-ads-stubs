from google.ads.googleads.v19.common.types.criteria import BrandInfo
from google.ads.googleads.v19.common.types.criteria import MobileApplicationInfo
from google.ads.googleads.v19.common.types.criteria import MobileAppCategoryInfo
from google.ads.googleads.v19.common.types.criteria import PlacementInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeVideoInfo
from google.ads.googleads.v19.common.types.criteria import KeywordInfo
from google.ads.googleads.v19.enums.types.criterion_type import CriterionTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., shared_set: str = ..., criterion_id: int = ..., type_: CriterionTypeEnum.CriterionType = ..., keyword: KeywordInfo = ..., youtube_video: YouTubeVideoInfo = ..., youtube_channel: YouTubeChannelInfo = ..., placement: PlacementInfo = ..., mobile_app_category: MobileAppCategoryInfo = ..., mobile_application: MobileApplicationInfo = ..., brand: BrandInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "shared_set", "criterion_id", "type_", "keyword", "youtube_video", "youtube_channel", "placement", "mobile_app_category", "mobile_application", "brand"]) -> bool: ...
