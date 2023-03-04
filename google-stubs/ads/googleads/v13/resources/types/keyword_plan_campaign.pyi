from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.enums.types.keyword_plan_network import (
    KeywordPlanNetworkEnum,
)

class KeywordPlanCampaign(proto.Message):
    resource_name: str
    keyword_plan: str
    id: int
    name: str
    language_constants: MutableSequence[str]
    keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork
    cpc_bid_micros: int
    geo_targets: MutableSequence[KeywordPlanGeoTarget]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        keyword_plan: str = ...,
        id: int = ...,
        name: str = ...,
        language_constants: MutableSequence[str] = ...,
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork = ...,
        cpc_bid_micros: int = ...,
        geo_targets: MutableSequence[KeywordPlanGeoTarget] = ...
    ) -> None: ...

class KeywordPlanGeoTarget(proto.Message):
    geo_target_constant: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        geo_target_constant: str = ...
    ) -> None: ...
