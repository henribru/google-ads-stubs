import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import keyword_match_type

__protobuf__: Incomplete

class KeywordPlanAdGroupKeyword(proto.Message):
    resource_name: str
    keyword_plan_ad_group: str
    id: int
    text: str
    match_type: keyword_match_type.KeywordMatchTypeEnum.KeywordMatchType
    cpc_bid_micros: int
    negative: bool
