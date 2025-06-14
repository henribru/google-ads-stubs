import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import data_link_status as gage_data_link_status
from google.ads.googleads.v20.resources.types import data_link as gagr_data_link

__protobuf__: Incomplete

class CreateDataLinkRequest(proto.Message):
    customer_id: str
    data_link: gagr_data_link.DataLink

class CreateDataLinkResponse(proto.Message):
    resource_name: str

class RemoveDataLinkRequest(proto.Message):
    customer_id: str
    resource_name: str

class RemoveDataLinkResponse(proto.Message):
    resource_name: str

class UpdateDataLinkRequest(proto.Message):
    customer_id: str
    data_link_status: gage_data_link_status.DataLinkStatusEnum.DataLinkStatus
    resource_name: str

class UpdateDataLinkResponse(proto.Message):
    resource_name: str
