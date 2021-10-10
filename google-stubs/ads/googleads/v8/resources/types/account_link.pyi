from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    account_link_status as account_link_status,
    linked_account_type as linked_account_type,
    mobile_app_vendor as mobile_app_vendor,
)

__protobuf__: Any

class AccountLink(proto.Message):
    resource_name: Any
    account_link_id: Any
    status: Any
    type_: Any
    third_party_app_analytics: Any
    data_partner: Any
    google_ads: Any

class ThirdPartyAppAnalyticsLinkIdentifier(proto.Message):
    app_analytics_provider_id: Any
    app_id: Any
    app_vendor: Any

class DataPartnerLinkIdentifier(proto.Message):
    data_partner_id: Any

class GoogleAdsLinkIdentifier(proto.Message):
    customer: Any
