from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.customizer_attribute_type import (
    CustomizerAttributeTypeEnum,
)

_M = TypeVar("_M")

class CustomizerValue(proto.Message):
    type_: CustomizerAttributeTypeEnum.CustomizerAttributeType
    string_value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: CustomizerAttributeTypeEnum.CustomizerAttributeType = ...,
        string_value: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_", "string_value"]
    ) -> bool: ...
