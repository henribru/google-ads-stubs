from typing import Any

import proto

from google.ads.googleads.v10.enums.types.account_link_status import (
    AccountLinkStatusEnum,
)
from google.ads.googleads.v10.enums.types.linked_account_type import (
    LinkedAccountTypeEnum,
)
from google.ads.googleads.v10.enums.types.mobile_app_vendor import MobileAppVendorEnum

class AccountLink(proto.Message):
    resource_name: str
    account_link_id: int
    status: AccountLinkStatusEnum.AccountLinkStatus
    type_: LinkedAccountTypeEnum.LinkedAccountType
    third_party_app_analytics: ThirdPartyAppAnalyticsLinkIdentifier
    data_partner: DataPartnerLinkIdentifier
    google_ads: GoogleAdsLinkIdentifier
    hotel_center: HotelCenterLinkIdentifier
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        account_link_id: int = ...,
        status: AccountLinkStatusEnum.AccountLinkStatus = ...,
        type_: LinkedAccountTypeEnum.LinkedAccountType = ...,
        third_party_app_analytics: ThirdPartyAppAnalyticsLinkIdentifier = ...,
        data_partner: DataPartnerLinkIdentifier = ...,
        google_ads: GoogleAdsLinkIdentifier = ...,
        hotel_center: HotelCenterLinkIdentifier = ...
    ) -> None: ...

class DataPartnerLinkIdentifier(proto.Message):
    data_partner_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        data_partner_id: int = ...
    ) -> None: ...

class GoogleAdsLinkIdentifier(proto.Message):
    customer: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer: str = ...
    ) -> None: ...

class HotelCenterLinkIdentifier(proto.Message):
    hotel_center_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        hotel_center_id: int = ...
    ) -> None: ...

class ThirdPartyAppAnalyticsLinkIdentifier(proto.Message):
    app_analytics_provider_id: int
    app_id: str
    app_vendor: MobileAppVendorEnum.MobileAppVendor
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        app_analytics_provider_id: int = ...,
        app_id: str = ...,
        app_vendor: MobileAppVendorEnum.MobileAppVendor = ...
    ) -> None: ...
