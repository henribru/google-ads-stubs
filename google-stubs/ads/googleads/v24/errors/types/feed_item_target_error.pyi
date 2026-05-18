from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FeedItemTargetErrorEnum(proto.Message):
    class FeedItemTargetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MUST_SET_TARGET_ONEOF_ON_CREATE = 2
        FEED_ITEM_TARGET_ALREADY_EXISTS = 3
        FEED_ITEM_SCHEDULES_CANNOT_OVERLAP = 4
        TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE = 5
        TOO_MANY_SCHEDULES_PER_DAY = 6
        CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS = 7
        DUPLICATE_AD_SCHEDULE = 8
        DUPLICATE_KEYWORD = 9

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
