from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdGroupFeedErrorEnum(proto.Message):
    class AdGroupFeedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 2
        CANNOT_CREATE_FOR_REMOVED_FEED = 3
        ADGROUP_FEED_ALREADY_EXISTS = 4
        CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED = 5
        INVALID_PLACEHOLDER_TYPE = 6
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = 7
        NO_EXISTING_LOCATION_CUSTOMER_FEED = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
