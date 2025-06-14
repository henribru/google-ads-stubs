import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import account_link_status, linked_account_type, mobile_app_vendor

__protobuf__: Incomplete

class AccountLink(proto.Message):
    resource_name: str
    account_link_id: int
    status: account_link_status.AccountLinkStatusEnum.AccountLinkStatus
    type_: linked_account_type.LinkedAccountTypeEnum.LinkedAccountType
    third_party_app_analytics: ThirdPartyAppAnalyticsLinkIdentifier

class ThirdPartyAppAnalyticsLinkIdentifier(proto.Message):
    app_analytics_provider_id: int
    app_id: str
    app_vendor: mobile_app_vendor.MobileAppVendorEnum.MobileAppVendor
