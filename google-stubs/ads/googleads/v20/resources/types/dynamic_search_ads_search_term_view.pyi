import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DynamicSearchAdsSearchTermView(proto.Message):
    resource_name: str
    search_term: str
    headline: str
    landing_page: str
    page_url: str
    has_negative_keyword: bool
    has_matching_keyword: bool
    has_negative_url: bool
