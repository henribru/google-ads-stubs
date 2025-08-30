from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FinalUrlExpansionAssetViewErrorEnum(proto.Message):
    class FinalUrlExpansionAssetViewError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MISSING_REQUIRED_FILTER = 2
        REQUIRES_ADVERTISING_CHANNEL_TYPE_FILTER = 3
        INVALID_ADVERTISING_CHANNEL_TYPE_IN_FILTER = 4
        CANNOT_SELECT_ASSET_GROUP = 5
        CANNOT_SELECT_AD_GROUP = 6
        REQUIRES_FILTER_BY_SINGLE_RESOURCE = 7
        CANNOT_SELECT_BOTH_AD_GROUP_AND_ASSET_GROUP = 8
        CANNOT_FILTER_BY_BOTH_AD_GROUP_AND_ASSET_GROUP = 9

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
