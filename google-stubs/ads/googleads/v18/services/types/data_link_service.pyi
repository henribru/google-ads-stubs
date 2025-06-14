import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import data_link as gagr_data_link

__protobuf__: Incomplete

class CreateDataLinkRequest(proto.Message):
    customer_id: str
    data_link: gagr_data_link.DataLink

class CreateDataLinkResponse(proto.Message):
    resource_name: str
