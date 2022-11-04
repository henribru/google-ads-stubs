from typing import Any

import proto

class AssetSetTypeEnum(proto.Message):
    class AssetSetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAGE_FEED = 2
        DYNAMIC_EDUCATION = 3
        MERCHANT_CENTER_FEED = 4
        DYNAMIC_REAL_ESTATE = 5
        DYNAMIC_CUSTOM = 6
        DYNAMIC_HOTELS_AND_RENTALS = 7
        DYNAMIC_FLIGHTS = 8
        DYNAMIC_TRAVEL = 9
        DYNAMIC_LOCAL = 10
        DYNAMIC_JOBS = 11
        LOCATION_SYNC = 12
        BUSINESS_PROFILE_DYNAMIC_LOCATION_GROUP = 13
        CHAIN_DYNAMIC_LOCATION_GROUP = 14
        STATIC_LOCATION_GROUP = 15
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
