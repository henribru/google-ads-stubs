import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import product_link as gagr_product_link

__protobuf__: Incomplete

class CreateProductLinkRequest(proto.Message):
    customer_id: str
    product_link: gagr_product_link.ProductLink

class CreateProductLinkResponse(proto.Message):
    resource_name: str

class RemoveProductLinkRequest(proto.Message):
    customer_id: str
    resource_name: str
    validate_only: bool

class RemoveProductLinkResponse(proto.Message):
    resource_name: str
