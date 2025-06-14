import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import linked_product_type, product_link_invitation_status

__protobuf__: Incomplete

class ProductLinkInvitation(proto.Message):
    resource_name: str
    product_link_invitation_id: int
    status: product_link_invitation_status.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    type_: linked_product_type.LinkedProductTypeEnum.LinkedProductType
    hotel_center: HotelCenterLinkInvitationIdentifier
    merchant_center: MerchantCenterLinkInvitationIdentifier
    advertising_partner: AdvertisingPartnerLinkInvitationIdentifier

class HotelCenterLinkInvitationIdentifier(proto.Message):
    hotel_center_id: int

class MerchantCenterLinkInvitationIdentifier(proto.Message):
    merchant_center_id: int

class AdvertisingPartnerLinkInvitationIdentifier(proto.Message):
    customer: str
