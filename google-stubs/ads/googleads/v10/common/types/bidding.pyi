from typing import Any

import proto

from google.ads.googleads.v10.enums.types.target_impression_share_location import (
    TargetImpressionShareLocationEnum,
)

class Commission(proto.Message):
    commission_rate_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        commission_rate_micros: int = ...,
    ) -> None: ...

class EnhancedCpc(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

class ManualCpc(proto.Message):
    enhanced_cpc_enabled: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        enhanced_cpc_enabled: bool = ...,
    ) -> None: ...

class ManualCpm(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

class ManualCpv(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

class MaximizeConversionValue(proto.Message):
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_roas: float = ...,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
    ) -> None: ...

class MaximizeConversions(proto.Message):
    target_cpa: int
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_cpa: int = ...,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
    ) -> None: ...

class PercentCpc(proto.Message):
    cpc_bid_ceiling_micros: int
    enhanced_cpc_enabled: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        cpc_bid_ceiling_micros: int = ...,
        enhanced_cpc_enabled: bool = ...,
    ) -> None: ...

class TargetCpa(proto.Message):
    target_cpa_micros: int
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_cpa_micros: int = ...,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
    ) -> None: ...

class TargetCpm(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

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
        cpc_bid_ceiling_micros: int = ...,
    ) -> None: ...

class TargetRoas(proto.Message):
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_roas: float = ...,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
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
        cpc_bid_ceiling_micros: int = ...,
    ) -> None: ...
