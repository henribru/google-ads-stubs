from typing import Any

import proto

class AdGroupErrorEnum(proto.Message):
    class AdGroupError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_ADGROUP_NAME = 2
        INVALID_ADGROUP_NAME = 3
        ADVERTISER_NOT_ON_CONTENT_NETWORK = 5
        BID_TOO_BIG = 6
        BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH = 7
        MISSING_ADGROUP_NAME = 8
        ADGROUP_LABEL_DOES_NOT_EXIST = 9
        ADGROUP_LABEL_ALREADY_EXISTS = 10
        INVALID_CONTENT_BID_CRITERION_TYPE_GROUP = 11
        AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE = 12
        ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY = 13
        CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING = 14
        PROMOTED_HOTEL_AD_GROUPS_NOT_AVAILABLE_FOR_CUSTOMER = 15
        INVALID_EXCLUDED_PARENT_ASSET_FIELD_TYPE = 16
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
