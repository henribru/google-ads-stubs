from typing import Any

import proto

from google.ads.googleads.v13.enums.types.customizer_attribute_type import (
    CustomizerAttributeTypeEnum,
)

class CustomizerValue(proto.Message):
    type_: CustomizerAttributeTypeEnum.CustomizerAttributeType
    string_value: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        type_: CustomizerAttributeTypeEnum.CustomizerAttributeType = ...,
        string_value: str = ...
    ) -> None: ...
