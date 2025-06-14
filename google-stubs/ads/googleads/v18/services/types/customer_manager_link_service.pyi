import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import customer_manager_link
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerManagerLinkRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerManagerLinkOperation']
    validate_only: bool

class MoveManagerLinkRequest(proto.Message):
    customer_id: str
    previous_customer_manager_link: str
    new_manager: str
    validate_only: bool

class CustomerManagerLinkOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    update: customer_manager_link.CustomerManagerLink

class MutateCustomerManagerLinkResponse(proto.Message):
    results: MutableSequence['MutateCustomerManagerLinkResult']

class MoveManagerLinkResponse(proto.Message):
    resource_name: str

class MutateCustomerManagerLinkResult(proto.Message):
    resource_name: str
