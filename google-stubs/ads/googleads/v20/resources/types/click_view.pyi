from google.ads.googleads.v20.common.types.criteria import KeywordInfo
from google.ads.googleads.v20.common.types.click_location import ClickLocation
from google.ads.googleads.v20.common.types.click_location import ClickLocation
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ClickView(proto.Message):
    resource_name: str
    gclid: str
    area_of_interest: ClickLocation
    location_of_presence: ClickLocation
    page_number: int
    ad_group_ad: str
    campaign_location_target: str
    user_list: str
    keyword: str
    keyword_info: KeywordInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., gclid: str = ..., area_of_interest: ClickLocation = ..., location_of_presence: ClickLocation = ..., page_number: int = ..., ad_group_ad: str = ..., campaign_location_target: str = ..., user_list: str = ..., keyword: str = ..., keyword_info: KeywordInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "gclid", "area_of_interest", "location_of_presence", "page_number", "ad_group_ad", "campaign_location_target", "user_list", "keyword", "keyword_info"]) -> bool: ...
