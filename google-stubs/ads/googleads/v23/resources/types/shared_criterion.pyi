from google.ads.googleads.v23.common.types.criteria import VerticalAdsItemGroupRuleInfo
from google.ads.googleads.v23.common.types.criteria import WebpageInfo
from google.ads.googleads.v23.common.types.criteria import BrandInfo
from google.ads.googleads.v23.common.types.criteria import MobileApplicationInfo
from google.ads.googleads.v23.common.types.criteria import MobileAppCategoryInfo
from google.ads.googleads.v23.common.types.criteria import PlacementInfo
from google.ads.googleads.v23.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v23.common.types.criteria import YouTubeVideoInfo
from google.ads.googleads.v23.common.types.criteria import KeywordInfo
from google.ads.googleads.v23.enums.types.criterion_type import CriterionTypeEnum
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
    negative: bool
    keyword: KeywordInfo
    youtube_video: YouTubeVideoInfo
    youtube_channel: YouTubeChannelInfo
    placement: PlacementInfo
    mobile_app_category: MobileAppCategoryInfo
    mobile_application: MobileApplicationInfo
    brand: BrandInfo
    webpage: WebpageInfo
    vertical_ads_item_group_rule: VerticalAdsItemGroupRuleInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., shared_set: str = ..., criterion_id: int = ..., type_: CriterionTypeEnum.CriterionType = ..., negative: bool = ..., keyword: KeywordInfo = ..., youtube_video: YouTubeVideoInfo = ..., youtube_channel: YouTubeChannelInfo = ..., placement: PlacementInfo = ..., mobile_app_category: MobileAppCategoryInfo = ..., mobile_application: MobileApplicationInfo = ..., brand: BrandInfo = ..., webpage: WebpageInfo = ..., vertical_ads_item_group_rule: VerticalAdsItemGroupRuleInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "shared_set", "criterion_id", "type_", "negative", "keyword", "youtube_video", "youtube_channel", "placement", "mobile_app_category", "mobile_application", "brand", "webpage", "vertical_ads_item_group_rule"]) -> bool: ...
