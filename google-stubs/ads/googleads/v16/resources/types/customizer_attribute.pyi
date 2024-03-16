from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.customizer_attribute_status import (
    CustomizerAttributeStatusEnum,
)
from google.ads.googleads.v16.enums.types.customizer_attribute_type import (
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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        type_: CustomizerAttributeTypeEnum.CustomizerAttributeType = ...,
        status: CustomizerAttributeStatusEnum.CustomizerAttributeStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "id", "name", "type_", "status"]
    ) -> bool: ...
