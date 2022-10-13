from typing import Any

import proto

from google.ads.googleads.v11.enums.types.keyword_match_type import KeywordMatchTypeEnum

class KeywordPlanCampaignKeyword(proto.Message):
    resource_name: str
    keyword_plan_campaign: str
    id: int
    text: str
    match_type: KeywordMatchTypeEnum.KeywordMatchType
    negative: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        keyword_plan_campaign: str = ...,
        id: int = ...,
        text: str = ...,
        match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        negative: bool = ...
    ) -> None: ...
