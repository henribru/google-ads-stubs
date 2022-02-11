from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v9.resources.types import (
    customer_client_link as customer_client_link,
)

__protobuf__: Any

class GetCustomerClientLinkRequest(proto.Message):
    resource_name: Any

class MutateCustomerClientLinkRequest(proto.Message):
    customer_id: Any
    operation: Any
    validate_only: Any

class CustomerClientLinkOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any

class MutateCustomerClientLinkResponse(proto.Message):
    result: Any

class MutateCustomerClientLinkResult(proto.Message):
    resource_name: Any
