from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.customizer_value import CustomizerValue
from google.ads.googleads.v14.enums.types.customizer_value_status import (
    CustomizerValueStatusEnum,
)

_M = TypeVar("_M")

class CustomerCustomizer(proto.Message):
    resource_name: str
    customizer_attribute: str
    status: CustomizerValueStatusEnum.CustomizerValueStatus
    value: CustomizerValue
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        customizer_attribute: str = ...,
        status: CustomizerValueStatusEnum.CustomizerValueStatus = ...,
        value: CustomizerValue = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "customizer_attribute", "status", "value"]
    ) -> bool: ...
