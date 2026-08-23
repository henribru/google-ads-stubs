from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetGroupPrimaryStatusReasonEnum(proto.Message):
    class AssetGroupPrimaryStatusReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ASSET_GROUP_PAUSED = 2
        ASSET_GROUP_REMOVED = 3
        CAMPAIGN_REMOVED = 4
        CAMPAIGN_PAUSED = 5
        CAMPAIGN_PENDING = 6
        CAMPAIGN_ENDED = 7
        ASSET_GROUP_LIMITED = 8
        ASSET_GROUP_DISAPPROVED = 9
        ASSET_GROUP_UNDER_REVIEW = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
