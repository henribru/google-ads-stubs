from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v8.resources.types import (
    merchant_center_link as merchant_center_link,
)

__protobuf__: Any

class ListMerchantCenterLinksRequest(proto.Message):
    customer_id: Any

class ListMerchantCenterLinksResponse(proto.Message):
    merchant_center_links: Any

class GetMerchantCenterLinkRequest(proto.Message):
    resource_name: Any

class MutateMerchantCenterLinkRequest(proto.Message):
    customer_id: Any
    operation: Any
    validate_only: Any

class MerchantCenterLinkOperation(proto.Message):
    update_mask: Any
    update: Any
    remove: Any

class MutateMerchantCenterLinkResponse(proto.Message):
    result: Any

class MutateMerchantCenterLinkResult(proto.Message):
    resource_name: Any
