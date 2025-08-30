from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetCoverageVideoAspectRatioRequirementEnum(proto.Message):
    class AssetCoverageVideoAspectRatioRequirement(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HORIZONTAL = 2
        SQUARE = 3
        VERTICAL = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
