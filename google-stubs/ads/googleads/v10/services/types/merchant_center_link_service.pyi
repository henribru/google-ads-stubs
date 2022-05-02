import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v10.resources.types import (
    merchant_center_link as merchant_center_link,
)

__protobuf__: Incomplete

class ListMerchantCenterLinksRequest(proto.Message):
    customer_id: Incomplete

class ListMerchantCenterLinksResponse(proto.Message):
    merchant_center_links: Incomplete

class GetMerchantCenterLinkRequest(proto.Message):
    resource_name: Incomplete

class MutateMerchantCenterLinkRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete
    validate_only: Incomplete

class MerchantCenterLinkOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateMerchantCenterLinkResponse(proto.Message):
    result: Incomplete

class MutateMerchantCenterLinkResult(proto.Message):
    resource_name: Incomplete
