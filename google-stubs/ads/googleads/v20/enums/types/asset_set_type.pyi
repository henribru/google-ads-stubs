import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetSetTypeEnum(proto.Message):
    class AssetSetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PAGE_FEED: int
        DYNAMIC_EDUCATION: int
        MERCHANT_CENTER_FEED: int
        DYNAMIC_REAL_ESTATE: int
        DYNAMIC_CUSTOM: int
        DYNAMIC_HOTELS_AND_RENTALS: int
        DYNAMIC_FLIGHTS: int
        DYNAMIC_TRAVEL: int
        DYNAMIC_LOCAL: int
        DYNAMIC_JOBS: int
        LOCATION_SYNC: int
        BUSINESS_PROFILE_DYNAMIC_LOCATION_GROUP: int
        CHAIN_DYNAMIC_LOCATION_GROUP: int
        STATIC_LOCATION_GROUP: int
        HOTEL_PROPERTY: int
        TRAVEL_FEED: int
