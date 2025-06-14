import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetCoverageVideoAspectRatioRequirementEnum(proto.Message):
    class AssetCoverageVideoAspectRatioRequirement(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HORIZONTAL = 2
        SQUARE = 3
        VERTICAL = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
