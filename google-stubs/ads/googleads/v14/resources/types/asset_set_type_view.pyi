from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.asset_set_type import AssetSetTypeEnum

_M = TypeVar("_M")

class AssetSetTypeView(proto.Message):
    resource_name: str
    asset_set_type: AssetSetTypeEnum.AssetSetType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_set_type: AssetSetTypeEnum.AssetSetType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "asset_set_type"]
    ) -> bool: ...
