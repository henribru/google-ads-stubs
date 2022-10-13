from typing import Any

import proto

from google.ads.googleads.v10.enums.types.conversion_custom_variable_status import (
    ConversionCustomVariableStatusEnum,
)

class ConversionCustomVariable(proto.Message):
    resource_name: str
    id: int
    name: str
    tag: str
    status: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    owner_customer: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        tag: str = ...,
        status: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus = ...,
        owner_customer: str = ...
    ) -> None: ...
