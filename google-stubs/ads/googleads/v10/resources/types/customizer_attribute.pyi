from typing import Any

import proto

from google.ads.googleads.v10.enums.types.customizer_attribute_status import (
    CustomizerAttributeStatusEnum,
)
from google.ads.googleads.v10.enums.types.customizer_attribute_type import (
    CustomizerAttributeTypeEnum,
)

class CustomizerAttribute(proto.Message):
    resource_name: str
    id: int
    name: str
    type_: CustomizerAttributeTypeEnum.CustomizerAttributeType
    status: CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        type_: CustomizerAttributeTypeEnum.CustomizerAttributeType = ...,
        status: CustomizerAttributeStatusEnum.CustomizerAttributeStatus = ...
    ) -> None: ...
