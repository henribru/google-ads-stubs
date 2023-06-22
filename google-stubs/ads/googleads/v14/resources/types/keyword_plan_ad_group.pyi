from typing import Any

import proto

class KeywordPlanAdGroup(proto.Message):
    resource_name: str
    keyword_plan_campaign: str
    id: int
    name: str
    cpc_bid_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        keyword_plan_campaign: str = ...,
        id: int = ...,
        name: str = ...,
        cpc_bid_micros: int = ...
    ) -> None: ...
