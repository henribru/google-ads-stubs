from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetSetErrorEnum(proto.Message):
    class AssetSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_ASSET_SET_NAME = 2
        INVALID_PARENT_ASSET_SET_TYPE = 3
        ASSET_SET_SOURCE_INCOMPATIBLE_WITH_PARENT_ASSET_SET = 4
        ASSET_SET_TYPE_CANNOT_BE_LINKED_TO_CUSTOMER = 5
        INVALID_CHAIN_IDS = 6
        LOCATION_SYNC_ASSET_SET_DOES_NOT_SUPPORT_RELATIONSHIP_TYPE = 7
        NOT_UNIQUE_ENABLED_LOCATION_SYNC_TYPED_ASSET_SET = 8
        INVALID_PLACE_IDS = 9
        OAUTH_INFO_INVALID = 11
        OAUTH_INFO_MISSING = 12
        CANNOT_DELETE_AS_ENABLED_LINKAGES_EXIST = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
