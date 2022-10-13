from typing import Any

import proto

from google.ads.googleads.v10.common.types.click_location import ClickLocation
from google.ads.googleads.v10.common.types.criteria import KeywordInfo

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        gclid: str = ...,
        area_of_interest: ClickLocation = ...,
        location_of_presence: ClickLocation = ...,
        page_number: int = ...,
        ad_group_ad: str = ...,
        campaign_location_target: str = ...,
        user_list: str = ...,
        keyword: str = ...,
        keyword_info: KeywordInfo = ...
    ) -> None: ...
