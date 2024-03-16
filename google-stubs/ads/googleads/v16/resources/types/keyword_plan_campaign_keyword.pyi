from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.keyword_match_type import KeywordMatchTypeEnum

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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        keyword_plan_campaign: str = ...,
        id: int = ...,
        text: str = ...,
        match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
        negative: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "keyword_plan_campaign",
            "id",
            "text",
            "match_type",
            "negative",
        ],
    ) -> bool: ...
