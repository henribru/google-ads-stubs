import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v10.resources.types import (
    customer_client_link as customer_client_link,
)

__protobuf__: Incomplete

class MutateCustomerClientLinkRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete
    validate_only: Incomplete

class CustomerClientLinkOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete

class MutateCustomerClientLinkResponse(proto.Message):
    result: Incomplete

class MutateCustomerClientLinkResult(proto.Message):
    resource_name: Incomplete
