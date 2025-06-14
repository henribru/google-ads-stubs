import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import search_term_targeting_status

__protobuf__: Incomplete

class SearchTermView(proto.Message):
    resource_name: str
    search_term: str
    ad_group: str
    status: search_term_targeting_status.SearchTermTargetingStatusEnum.SearchTermTargetingStatus
