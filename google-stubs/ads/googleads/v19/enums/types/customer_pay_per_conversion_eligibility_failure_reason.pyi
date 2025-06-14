import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomerPayPerConversionEligibilityFailureReasonEnum(proto.Message):
    class CustomerPayPerConversionEligibilityFailureReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_ENOUGH_CONVERSIONS: int
        CONVERSION_LAG_TOO_HIGH: int
        HAS_CAMPAIGN_WITH_SHARED_BUDGET: int
        HAS_UPLOAD_CLICKS_CONVERSION: int
        AVERAGE_DAILY_SPEND_TOO_HIGH: int
        ANALYSIS_NOT_COMPLETE: int
        OTHER: int
