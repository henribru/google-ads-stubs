from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    manager_link_status as manager_link_status,
)

__protobuf__: Any

class CustomerClientLink(proto.Message):
    resource_name: Any
    client_customer: Any
    manager_link_id: Any
    status: Any
    hidden: Any
