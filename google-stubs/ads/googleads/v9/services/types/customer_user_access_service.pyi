from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v9.resources.types import (
    customer_user_access as customer_user_access,
)

__protobuf__: Any

class GetCustomerUserAccessRequest(proto.Message):
    resource_name: Any

class MutateCustomerUserAccessRequest(proto.Message):
    customer_id: Any
    operation: Any

class CustomerUserAccessOperation(proto.Message):
    update_mask: Any
    update: Any
    remove: Any

class MutateCustomerUserAccessResponse(proto.Message):
    result: Any

class MutateCustomerUserAccessResult(proto.Message):
    resource_name: Any
