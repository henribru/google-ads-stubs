from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.served_asset_field_type import (
    ServedAssetFieldTypeEnum,
)

_M = TypeVar("_M")

class AssetUsage(proto.Message):
    asset: str
    served_asset_field_type: ServedAssetFieldTypeEnum.ServedAssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset: str = ...,
        served_asset_field_type: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset", "served_asset_field_type"]
    ) -> bool: ...
