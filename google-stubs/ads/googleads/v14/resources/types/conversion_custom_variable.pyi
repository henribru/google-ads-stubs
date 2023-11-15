from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.conversion_custom_variable_status import (
    ConversionCustomVariableStatusEnum,
)

_M = TypeVar("_M")

class ConversionCustomVariable(proto.Message):
    resource_name: str
    id: int
    name: str
    tag: str
    status: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    owner_customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        tag: str = ...,
        status: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus = ...,
        owner_customer: str = ...
    ) -> None: ...
