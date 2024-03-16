from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CampaignFeedErrorEnum(proto.Message):
    class CampaignFeedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 2
        CANNOT_CREATE_FOR_REMOVED_FEED = 4
        CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED = 5
        CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED = 6
        INVALID_PLACEHOLDER_TYPE = 7
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = 8
        NO_EXISTING_LOCATION_CUSTOMER_FEED = 9
        LEGACY_FEED_TYPE_READ_ONLY = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
