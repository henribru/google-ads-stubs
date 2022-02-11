from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    customizer_attribute_status as customizer_attribute_status,
    customizer_attribute_type as customizer_attribute_type,
)

__protobuf__: Any

class CustomizerAttribute(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    type_: Any
    status: Any
