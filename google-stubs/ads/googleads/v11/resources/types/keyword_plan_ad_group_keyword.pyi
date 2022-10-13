from typing import Any

import proto

from google.ads.googleads.v11.enums.types.keyword_match_type import KeywordMatchTypeEnum

class KeywordPlanAdGroupKeyword(proto.Message):
    resource_name: str
    keyword_plan_ad_group: str
    id: int
    text: str
    match_type: KeywordMatchTypeEnum.KeywordMatchType
    cpc_bid_micros: int
    negative: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        keyword_plan_ad_group: str = ...,
        id: int = ...,
        text: str = ...,
        match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        cpc_bid_micros: int = ...,
        negative: bool = ...
    ) -> None: ...
