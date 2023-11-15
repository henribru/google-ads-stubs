from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.click_location import ClickLocation
from google.ads.googleads.v15.common.types.criteria import KeywordInfo

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
