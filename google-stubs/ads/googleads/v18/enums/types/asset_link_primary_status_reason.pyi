from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetLinkPrimaryStatusReasonEnum(proto.Message):
    class AssetLinkPrimaryStatusReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ASSET_LINK_PAUSED = 2
        ASSET_LINK_REMOVED = 3
        ASSET_DISAPPROVED = 4
        ASSET_UNDER_REVIEW = 5
        ASSET_APPROVED_LABELED = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
