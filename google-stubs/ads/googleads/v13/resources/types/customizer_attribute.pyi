from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.customizer_attribute_status import (
    CustomizerAttributeStatusEnum,
)
from google.ads.googleads.v13.enums.types.customizer_attribute_type import (
    CustomizerAttributeTypeEnum,
)

_M = TypeVar("_M")

class CustomizerAttribute(proto.Message):
    resource_name: str
    id: int
    name: str
    type_: CustomizerAttributeTypeEnum.CustomizerAttributeType
    status: CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        type_: CustomizerAttributeTypeEnum.CustomizerAttributeType = ...,
        status: CustomizerAttributeStatusEnum.CustomizerAttributeStatus = ...
    ) -> None: ...
