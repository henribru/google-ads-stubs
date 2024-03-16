from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ChangeStatusResourceTypeEnum(proto.Message):
    class ChangeStatusResourceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP = 3
        AD_GROUP_AD = 4
        AD_GROUP_CRITERION = 5
        CAMPAIGN = 6
        CAMPAIGN_CRITERION = 7
        FEED = 9
        FEED_ITEM = 10
        AD_GROUP_FEED = 11
        CAMPAIGN_FEED = 12
        AD_GROUP_BID_MODIFIER = 13
        SHARED_SET = 14
        CAMPAIGN_SHARED_SET = 15
        ASSET = 16
        CUSTOMER_ASSET = 17
        CAMPAIGN_ASSET = 18
        AD_GROUP_ASSET = 19
        COMBINED_AUDIENCE = 20

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
