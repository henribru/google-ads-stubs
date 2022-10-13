from typing import Any

import proto

from google.ads.googleads.v11.enums.types.bidding_strategy_type import (
    BiddingStrategyTypeEnum,
)
from google.ads.googleads.v11.enums.types.target_impression_share_location import (
    TargetImpressionShareLocationEnum,
)

class AccessibleBiddingStrategy(proto.Message):
    class MaximizeConversionValue(proto.Message):
        target_roas: float
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_roas: float = ...
        ) -> None: ...

    class MaximizeConversions(proto.Message):
        target_cpa_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_cpa_micros: int = ...
        ) -> None: ...

    class TargetCpa(proto.Message):
        target_cpa_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_cpa_micros: int = ...
        ) -> None: ...

    class TargetImpressionShare(proto.Message):
        location: TargetImpressionShareLocationEnum.TargetImpressionShareLocation
        location_fraction_micros: int
        cpc_bid_ceiling_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            location: TargetImpressionShareLocationEnum.TargetImpressionShareLocation = ...,
            location_fraction_micros: int = ...,
            cpc_bid_ceiling_micros: int = ...
        ) -> None: ...

    class TargetRoas(proto.Message):
        target_roas: float
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_roas: float = ...
        ) -> None: ...

    class TargetSpend(proto.Message):
        target_spend_micros: int
        cpc_bid_ceiling_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_spend_micros: int = ...,
            cpc_bid_ceiling_micros: int = ...
        ) -> None: ...
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        target_spend: AccessibleBiddingStrategy.TargetSpend = ...
    ) -> None: ...
