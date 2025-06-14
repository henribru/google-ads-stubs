import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import keyword_match_type

__protobuf__: Incomplete

class KeywordPlanCampaignKeyword(proto.Message):
    resource_name: str
    keyword_plan_campaign: str
    id: int
    text: str
    match_type: keyword_match_type.KeywordMatchTypeEnum.KeywordMatchType
    negative: bool
