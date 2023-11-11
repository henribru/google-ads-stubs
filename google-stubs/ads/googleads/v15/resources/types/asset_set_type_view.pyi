from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.asset_set_type import AssetSetTypeEnum

_M = TypeVar("_M")

class AssetSetTypeView(proto.Message):
    resource_name: str
    asset_set_type: AssetSetTypeEnum.AssetSetType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_set_type: AssetSetTypeEnum.AssetSetType = ...
    ) -> None: ...
