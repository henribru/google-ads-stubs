from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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
