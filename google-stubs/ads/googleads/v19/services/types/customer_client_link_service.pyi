import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import customer_client_link
from google.protobuf import field_mask_pb2

__protobuf__: Incomplete

class MutateCustomerClientLinkRequest(proto.Message):
    customer_id: str
    operation: CustomerClientLinkOperation
    validate_only: bool

class CustomerClientLinkOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: customer_client_link.CustomerClientLink
    update: customer_client_link.CustomerClientLink

class MutateCustomerClientLinkResponse(proto.Message):
    result: MutateCustomerClientLinkResult

class MutateCustomerClientLinkResult(proto.Message):
    resource_name: str
