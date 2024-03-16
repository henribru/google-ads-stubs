from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.account_link_status import (
    AccountLinkStatusEnum,
)
from google.ads.googleads.v16.enums.types.linked_account_type import (
    LinkedAccountTypeEnum,
)
from google.ads.googleads.v16.enums.types.mobile_app_vendor import MobileAppVendorEnum

_M = TypeVar("_M")

class AccountLink(proto.Message):
    resource_name: str
    account_link_id: int
    status: AccountLinkStatusEnum.AccountLinkStatus
    type_: LinkedAccountTypeEnum.LinkedAccountType
    third_party_app_analytics: ThirdPartyAppAnalyticsLinkIdentifier
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
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "account_link_id",
            "status",
            "type_",
            "third_party_app_analytics",
        ],
    ) -> bool: ...

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
        app_vendor: MobileAppVendorEnum.MobileAppVendor = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["app_analytics_provider_id", "app_id", "app_vendor"]
    ) -> bool: ...
