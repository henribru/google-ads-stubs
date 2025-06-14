import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DomainCategory(proto.Message):
    resource_name: str
    campaign: str
    category: str
    language_code: str
    domain: str
    coverage_fraction: float
    category_rank: int
    has_children: bool
    recommended_cpc_bid_micros: int
