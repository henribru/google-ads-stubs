from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.keyword_plan_network import (
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
        geo_targets: MutableSequence[KeywordPlanGeoTarget] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "keyword_plan",
            "id",
            "name",
            "language_constants",
            "keyword_plan_network",
            "cpc_bid_micros",
            "geo_targets",
        ],
    ) -> bool: ...

class KeywordPlanGeoTarget(proto.Message):
    geo_target_constant: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_target_constant: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["geo_target_constant"]
    ) -> bool: ...
