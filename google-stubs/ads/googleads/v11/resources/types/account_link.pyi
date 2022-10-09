import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    account_link_status as account_link_status,
    linked_account_type as linked_account_type,
    mobile_app_vendor as mobile_app_vendor,
)

__protobuf__: Incomplete

class AccountLink(proto.Message):
    resource_name: Incomplete
    account_link_id: Incomplete
    status: Incomplete
    type_: Incomplete
    third_party_app_analytics: Incomplete
    data_partner: Incomplete
    google_ads: Incomplete
    hotel_center: Incomplete

class ThirdPartyAppAnalyticsLinkIdentifier(proto.Message):
    app_analytics_provider_id: Incomplete
    app_id: Incomplete
    app_vendor: Incomplete

class DataPartnerLinkIdentifier(proto.Message):
    data_partner_id: Incomplete

class HotelCenterLinkIdentifier(proto.Message):
    hotel_center_id: Incomplete

class GoogleAdsLinkIdentifier(proto.Message):
    customer: Incomplete
