import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import product_link_invitation_status as gage_product_link_invitation_status
from google.ads.googleads.v18.resources.types import product_link_invitation as gagr_product_link_invitation

__protobuf__: Incomplete

class CreateProductLinkInvitationRequest(proto.Message):
    customer_id: str
    product_link_invitation: gagr_product_link_invitation.ProductLinkInvitation

class CreateProductLinkInvitationResponse(proto.Message):
    resource_name: str

class UpdateProductLinkInvitationRequest(proto.Message):
    customer_id: str
    product_link_invitation_status: gage_product_link_invitation_status.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    resource_name: str

class UpdateProductLinkInvitationResponse(proto.Message):
    resource_name: str

class RemoveProductLinkInvitationRequest(proto.Message):
    customer_id: str
    resource_name: str

class RemoveProductLinkInvitationResponse(proto.Message):
    resource_name: str
