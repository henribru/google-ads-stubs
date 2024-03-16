from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.asset_field_type import AssetFieldTypeEnum

_M = TypeVar("_M")

class AssetFieldTypeView(proto.Message):
    resource_name: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "field_type"]
    ) -> bool: ...
