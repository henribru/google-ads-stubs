from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.customizer_attribute_type import (
    CustomizerAttributeTypeEnum,
)

_M = TypeVar("_M")

class CustomizerValue(proto.Message):
    type_: CustomizerAttributeTypeEnum.CustomizerAttributeType
    string_value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        type_: CustomizerAttributeTypeEnum.CustomizerAttributeType = ...,
        string_value: str = ...
    ) -> None: ...
