from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.keyword_match_type import KeywordMatchTypeEnum

_M = TypeVar("_M")

class KeywordPlanAdGroupKeyword(proto.Message):
    resource_name: str
    keyword_plan_ad_group: str
    id: int
    text: str
    match_type: KeywordMatchTypeEnum.KeywordMatchType
    cpc_bid_micros: int
    negative: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        keyword_plan_ad_group: str = ...,
        id: int = ...,
        text: str = ...,
        match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        cpc_bid_micros: int = ...,
        negative: bool = ...
    ) -> None: ...
