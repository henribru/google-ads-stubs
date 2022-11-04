from typing import Any

import proto

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        category: str = ...,
        language_code: str = ...,
        domain: str = ...,
        coverage_fraction: float = ...,
        category_rank: int = ...,
        has_children: bool = ...,
        recommended_cpc_bid_micros: int = ...
    ) -> None: ...
