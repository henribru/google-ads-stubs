from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.account_link_status import (
    AccountLinkStatusEnum,
)
from google.ads.googleads.v14.enums.types.linked_account_type import (
    LinkedAccountTypeEnum,
)
from google.ads.googleads.v14.enums.types.mobile_app_vendor import MobileAppVendorEnum

_M = TypeVar("_M")

class AccountLink(proto.Message):
    resource_name: str
    account_link_id: int
    status: AccountLinkStatusEnum.AccountLinkStatus
    type_: LinkedAccountTypeEnum.LinkedAccountType
    third_party_app_analytics: ThirdPartyAppAnalyticsLinkIdentifier
    data_partner: DataPartnerLinkIdentifier
    google_ads: GoogleAdsLinkIdentifier
    hotel_center: HotelCenterLinkIdentifier
    advertising_partner: AdvertisingPartnerLinkIdentifier
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        account_link_id: int = ...,
        status: AccountLinkStatusEnum.AccountLinkStatus = ...,
        type_: LinkedAccountTypeEnum.LinkedAccountType = ...,
        third_party_app_analytics: ThirdPartyAppAnalyticsLinkIdentifier = ...,
        data_partner: DataPartnerLinkIdentifier = ...,
        google_ads: GoogleAdsLinkIdentifier = ...,
        hotel_center: HotelCenterLinkIdentifier = ...,
        advertising_partner: AdvertisingPartnerLinkIdentifier = ...
    ) -> None: ...

class AdvertisingPartnerLinkIdentifier(proto.Message):
    customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer: str = ...
    ) -> None: ...

class DataPartnerLinkIdentifier(proto.Message):
    data_partner_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data_partner_id: int = ...
    ) -> None: ...

class GoogleAdsLinkIdentifier(proto.Message):
    customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer: str = ...
    ) -> None: ...

class HotelCenterLinkIdentifier(proto.Message):
    hotel_center_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        hotel_center_id: int = ...
    ) -> None: ...

class ThirdPartyAppAnalyticsLinkIdentifier(proto.Message):
    app_analytics_provider_id: int
    app_id: str
    app_vendor: MobileAppVendorEnum.MobileAppVendor
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        app_analytics_provider_id: int = ...,
        app_id: str = ...,
        app_vendor: MobileAppVendorEnum.MobileAppVendor = ...
    ) -> None: ...
