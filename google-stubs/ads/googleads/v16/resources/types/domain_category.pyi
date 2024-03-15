from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    def __contains__(self, key: Literal["resource_name", "campaign", "category", "language_code", "domain", "coverage_fraction", "category_rank", "has_children", "recommended_cpc_bid_micros"]) -> bool: ...  # type: ignore[override]
