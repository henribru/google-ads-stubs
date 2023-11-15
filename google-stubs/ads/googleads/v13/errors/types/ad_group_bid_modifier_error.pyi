from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdGroupBidModifierErrorEnum(proto.Message):
    class AdGroupBidModifierError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CRITERION_ID_NOT_SUPPORTED = 2
        CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
