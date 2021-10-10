from typing import Any

import proto

__protobuf__: Any

class FeedItemTargetErrorEnum(proto.Message):
    class FeedItemTargetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MUST_SET_TARGET_ONEOF_ON_CREATE: int
        FEED_ITEM_TARGET_ALREADY_EXISTS: int
        FEED_ITEM_SCHEDULES_CANNOT_OVERLAP: int
        TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE: int
        TOO_MANY_SCHEDULES_PER_DAY: int
        CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS: int
        DUPLICATE_AD_SCHEDULE: int
        DUPLICATE_KEYWORD: int
