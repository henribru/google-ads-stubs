from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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
        field_type: AssetFieldTypeEnum.AssetFieldType = ...
    ) -> None: ...
