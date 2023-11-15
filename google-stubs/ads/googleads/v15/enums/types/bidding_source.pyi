from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class BiddingSourceEnum(proto.Message):
    class BiddingSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_BIDDING_STRATEGY = 5
        AD_GROUP = 6
        AD_GROUP_CRITERION = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
