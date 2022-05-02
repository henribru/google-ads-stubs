import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v10.resources.types import (
    customer_manager_link as customer_manager_link,
)

__protobuf__: Incomplete

class MutateCustomerManagerLinkRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete

class MoveManagerLinkRequest(proto.Message):
    customer_id: Incomplete
    previous_customer_manager_link: Incomplete
    new_manager: Incomplete
    validate_only: Incomplete

class CustomerManagerLinkOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete

class MutateCustomerManagerLinkResponse(proto.Message):
    results: Incomplete

class MoveManagerLinkResponse(proto.Message):
    resource_name: Incomplete

class MutateCustomerManagerLinkResult(proto.Message):
    resource_name: Incomplete
