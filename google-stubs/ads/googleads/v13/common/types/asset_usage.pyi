from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.served_asset_field_type import (
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
        served_asset_field_type: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...
    ) -> None: ...
