from google.ads.googleads.v19.common.types.criteria import IpBlockInfo
from google.ads.googleads.v19.common.types.criteria import NegativeKeywordListInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v19.common.types.criteria import YouTubeVideoInfo
from google.ads.googleads.v19.common.types.criteria import PlacementInfo
from google.ads.googleads.v19.common.types.criteria import MobileAppCategoryInfo
from google.ads.googleads.v19.common.types.criteria import MobileApplicationInfo
from google.ads.googleads.v19.common.types.criteria import ContentLabelInfo
from google.ads.googleads.v19.enums.types.criterion_type import CriterionTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., id: int = ..., type_: CriterionTypeEnum.CriterionType = ..., content_label: ContentLabelInfo = ..., mobile_application: MobileApplicationInfo = ..., mobile_app_category: MobileAppCategoryInfo = ..., placement: PlacementInfo = ..., youtube_video: YouTubeVideoInfo = ..., youtube_channel: YouTubeChannelInfo = ..., negative_keyword_list: NegativeKeywordListInfo = ..., ip_block: IpBlockInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "type_", "content_label", "mobile_application", "mobile_app_category", "placement", "youtube_video", "youtube_channel", "negative_keyword_list", "ip_block"]) -> bool: ...
