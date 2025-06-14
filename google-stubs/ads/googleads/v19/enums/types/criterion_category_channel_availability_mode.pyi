import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CriterionCategoryChannelAvailabilityModeEnum(proto.Message):
    class CriterionCategoryChannelAvailabilityMode(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ALL_CHANNELS: int
        CHANNEL_TYPE_AND_ALL_SUBTYPES: int
        CHANNEL_TYPE_AND_SUBSET_SUBTYPES: int
