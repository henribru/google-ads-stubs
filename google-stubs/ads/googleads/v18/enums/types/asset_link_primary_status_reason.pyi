import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
