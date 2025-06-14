from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class KeywordPlanAdGroup(proto.Message):
    resource_name: str
    keyword_plan_campaign: str
    id: int
    name: str
    cpc_bid_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        keyword_plan_campaign: str = ...,
        id: int = ...,
        name: str = ...,
        cpc_bid_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "keyword_plan_campaign", "id", "name", "cpc_bid_micros"
        ],
    ) -> bool: ...
