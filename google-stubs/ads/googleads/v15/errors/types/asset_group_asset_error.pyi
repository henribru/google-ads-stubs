from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AssetGroupAssetErrorEnum(proto.Message):
    class AssetGroupAssetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_RESOURCE = 2
        EXPANDABLE_TAGS_NOT_ALLOWED_IN_DESCRIPTION = 3
        AD_CUSTOMIZER_NOT_SUPPORTED = 4
        HOTEL_PROPERTY_ASSET_NOT_LINKED_TO_CAMPAIGN = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
