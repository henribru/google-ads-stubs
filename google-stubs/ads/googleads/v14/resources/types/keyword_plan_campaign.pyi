from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.keyword_plan_network import (
    KeywordPlanNetworkEnum,
)

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_target_constant: str = ...
    ) -> None: ...
