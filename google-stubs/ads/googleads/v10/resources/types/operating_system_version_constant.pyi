from typing import Any

import proto

from google.ads.googleads.v10.enums.types.operating_system_version_operator_type import (
    OperatingSystemVersionOperatorTypeEnum,
)

class OperatingSystemVersionConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    os_major_version: int
    os_minor_version: int
    operator_type: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        os_major_version: int = ...,
        os_minor_version: int = ...,
        operator_type: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType = ...
    ) -> None: ...
