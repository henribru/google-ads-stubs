from google.ads.googleads.v23.enums.types.keyword_match_type import KeywordMatchTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class KeywordPlanAdGroupKeyword(proto.Message):
    resource_name: str
    keyword_plan_ad_group: str
    id: int
    text: str
    match_type: KeywordMatchTypeEnum.KeywordMatchType
    cpc_bid_micros: int
    negative: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., keyword_plan_ad_group: str = ..., id: int = ..., text: str = ..., match_type: KeywordMatchTypeEnum.KeywordMatchType = ..., cpc_bid_micros: int = ..., negative: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "keyword_plan_ad_group", "id", "text", "match_type", "cpc_bid_micros", "negative"]) -> bool: ...
