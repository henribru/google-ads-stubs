from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.operating_system_version_operator_type import (
    OperatingSystemVersionOperatorTypeEnum,
)

_M = TypeVar("_M")

class OperatingSystemVersionConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    os_major_version: int
    os_minor_version: int
    operator_type: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        os_major_version: int = ...,
        os_minor_version: int = ...,
        operator_type: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType = ...
    ) -> None: ...
