from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetSetAssetErrorEnum(proto.Message):
    class AssetSetAssetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_ASSET_TYPE = 2
        INVALID_ASSET_SET_TYPE = 3
        DUPLICATE_EXTERNAL_KEY = 4
        PARENT_LINKAGE_DOES_NOT_EXIST = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
