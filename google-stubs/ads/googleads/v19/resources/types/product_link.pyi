import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import linked_product_type

__protobuf__: Incomplete

class ProductLink(proto.Message):
    resource_name: str
    product_link_id: int
    type_: linked_product_type.LinkedProductTypeEnum.LinkedProductType
    data_partner: DataPartnerIdentifier
    google_ads: GoogleAdsIdentifier
    merchant_center: MerchantCenterIdentifier
    advertising_partner: AdvertisingPartnerIdentifier

class DataPartnerIdentifier(proto.Message):
    data_partner_id: int

class GoogleAdsIdentifier(proto.Message):
    customer: str

class MerchantCenterIdentifier(proto.Message):
    merchant_center_id: int

class AdvertisingPartnerIdentifier(proto.Message):
    customer: str
