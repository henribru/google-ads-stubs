import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SmartCampaignErrorEnum(proto.Message):
    class SmartCampaignError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_BUSINESS_LOCATION_ID: int
        INVALID_CAMPAIGN: int
        BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING: int
        REQUIRED_SUGGESTION_FIELD_MISSING: int
        GEO_TARGETS_REQUIRED: int
        CANNOT_DETERMINE_SUGGESTION_LOCALE: int
        FINAL_URL_NOT_CRAWLABLE: int
