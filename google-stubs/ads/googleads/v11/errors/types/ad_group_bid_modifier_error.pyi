import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdGroupBidModifierErrorEnum(proto.Message):
    class AdGroupBidModifierError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CRITERION_ID_NOT_SUPPORTED: int
        CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER: int
