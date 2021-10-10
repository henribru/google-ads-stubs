from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    shared_set_status as shared_set_status,
    shared_set_type as shared_set_type,
)

__protobuf__: Any

class SharedSet(proto.Message):
    resource_name: Any
    id: Any
    type_: Any
    name: Any
    status: Any
    member_count: Any
    reference_count: Any
