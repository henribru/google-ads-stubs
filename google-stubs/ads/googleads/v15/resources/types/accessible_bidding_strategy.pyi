from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.bidding_strategy_type import (
    BiddingStrategyTypeEnum,
)
from google.ads.googleads.v15.enums.types.target_impression_share_location import (
    TargetImpressionShareLocationEnum,
)

_M = TypeVar("_M")

class AccessibleBiddingStrategy(proto.Message):
    class MaximizeConversionValue(proto.Message):
        target_roas: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_roas: float = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["target_roas"]
        ) -> bool: ...

    class MaximizeConversions(proto.Message):
        target_cpa_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_cpa_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["target_cpa_micros"]
        ) -> bool: ...

    class TargetCpa(proto.Message):
        target_cpa_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_cpa_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["target_cpa_micros"]
        ) -> bool: ...

    class TargetImpressionShare(proto.Message):
        location: TargetImpressionShareLocationEnum.TargetImpressionShareLocation
        location_fraction_micros: int
        cpc_bid_ceiling_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            location: TargetImpressionShareLocationEnum.TargetImpressionShareLocation = ...,
            location_fraction_micros: int = ...,
            cpc_bid_ceiling_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "location", "location_fraction_micros", "cpc_bid_ceiling_micros"
            ],
        ) -> bool: ...

    class TargetRoas(proto.Message):
        target_roas: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_roas: float = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["target_roas"]
        ) -> bool: ...

    class TargetSpend(proto.Message):
        target_spend_micros: int
        cpc_bid_ceiling_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_spend_micros: int = ...,
            cpc_bid_ceiling_micros: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["target_spend_micros", "cpc_bid_ceiling_micros"]
        ) -> bool: ...

    resource_name: str
    id: int
    name: str
    type_: BiddingStrategyTypeEnum.BiddingStrategyType
    owner_customer_id: int
    owner_descriptive_name: str
    maximize_conversion_value: AccessibleBiddingStrategy.MaximizeConversionValue
    maximize_conversions: AccessibleBiddingStrategy.MaximizeConversions
    target_cpa: AccessibleBiddingStrategy.TargetCpa
    target_impression_share: AccessibleBiddingStrategy.TargetImpressionShare
    target_roas: AccessibleBiddingStrategy.TargetRoas
    target_spend: AccessibleBiddingStrategy.TargetSpend
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        type_: BiddingStrategyTypeEnum.BiddingStrategyType = ...,
        owner_customer_id: int = ...,
        owner_descriptive_name: str = ...,
        maximize_conversion_value: AccessibleBiddingStrategy.MaximizeConversionValue = ...,
        maximize_conversions: AccessibleBiddingStrategy.MaximizeConversions = ...,
        target_cpa: AccessibleBiddingStrategy.TargetCpa = ...,
        target_impression_share: AccessibleBiddingStrategy.TargetImpressionShare = ...,
        target_roas: AccessibleBiddingStrategy.TargetRoas = ...,
        target_spend: AccessibleBiddingStrategy.TargetSpend = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "name",
            "type_",
            "owner_customer_id",
            "owner_descriptive_name",
            "maximize_conversion_value",
            "maximize_conversions",
            "target_cpa",
            "target_impression_share",
            "target_roas",
            "target_spend",
        ],
    ) -> bool: ...
