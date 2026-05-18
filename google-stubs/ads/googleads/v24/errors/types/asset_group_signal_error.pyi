from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetGroupSignalErrorEnum(proto.Message):
    class AssetGroupSignalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TOO_MANY_WORDS = 2
        SEARCH_THEME_POLICY_VIOLATION = 3
        AUDIENCE_WITH_WRONG_ASSET_GROUP_ID = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
