from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.keyword_match_type import KeywordMatchTypeEnum

_M = TypeVar("_M")

class KeywordPlanCampaignKeyword(proto.Message):
    resource_name: str
    keyword_plan_campaign: str
    id: int
    text: str
    match_type: KeywordMatchTypeEnum.KeywordMatchType
    negative: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        keyword_plan_campaign: str = ...,
        id: int = ...,
        text: str = ...,
        match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        negative: bool = ...
    ) -> None: ...
