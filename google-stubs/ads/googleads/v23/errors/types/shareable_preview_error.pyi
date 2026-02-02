import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ShareablePreviewErrorEnum(proto.Message):
    class ShareablePreviewError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TOO_MANY_ASSET_GROUPS_IN_REQUEST = 2
        ASSET_GROUP_DOES_NOT_EXIST_UNDER_THIS_CUSTOMER = 3
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
