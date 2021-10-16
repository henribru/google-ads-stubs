from typing import Any

import proto

__protobuf__: Any

class FeedErrorEnum(proto.Message):
    class FeedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ATTRIBUTE_NAMES_NOT_UNIQUE: int
        ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES: int
        CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED: int
        CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED: int
        CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED: int
        CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE: int
        FEED_REMOVED: int
        INVALID_ORIGIN_VALUE: int
        FEED_ORIGIN_IS_NOT_USER: int
        INVALID_AUTH_TOKEN_FOR_EMAIL: int
        INVALID_EMAIL: int
        DUPLICATE_FEED_NAME: int
        INVALID_FEED_NAME: int
        MISSING_OAUTH_INFO: int
        NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY: int
        TOO_MANY_ATTRIBUTES: int
        INVALID_BUSINESS_ACCOUNT: int
        BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT: int
        INVALID_AFFILIATE_CHAIN_ID: int
        DUPLICATE_SYSTEM_FEED: int
        GMB_ACCESS_ERROR: int
        CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS: int
