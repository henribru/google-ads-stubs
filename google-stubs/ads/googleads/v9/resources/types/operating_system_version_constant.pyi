from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    operating_system_version_operator_type as operating_system_version_operator_type,
)

__protobuf__: Any

class OperatingSystemVersionConstant(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    os_major_version: Any
    os_minor_version: Any
    operator_type: Any
