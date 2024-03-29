from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FeedErrorEnum(proto.Message):
    class FeedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ATTRIBUTE_NAMES_NOT_UNIQUE = 2
        ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES = 3
        CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED = 4
        CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED = 5
        CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED = 6
        CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE = 7
        FEED_REMOVED = 8
        INVALID_ORIGIN_VALUE = 9
        FEED_ORIGIN_IS_NOT_USER = 10
        INVALID_AUTH_TOKEN_FOR_EMAIL = 11
        INVALID_EMAIL = 12
        DUPLICATE_FEED_NAME = 13
        INVALID_FEED_NAME = 14
        MISSING_OAUTH_INFO = 15
        NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY = 16
        TOO_MANY_ATTRIBUTES = 17
        INVALID_BUSINESS_ACCOUNT = 18
        BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT = 19
        INVALID_AFFILIATE_CHAIN_ID = 20
        DUPLICATE_SYSTEM_FEED = 21
        GMB_ACCESS_ERROR = 22
        CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS = 23
        LEGACY_EXTENSION_TYPE_READ_ONLY = 24

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
