import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class HotelAssetSuggestionStatusEnum(proto.Message):
    class HotelAssetSuggestionStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SUCCESS: int
        HOTEL_NOT_FOUND: int
        INVALID_PLACE_ID: int
