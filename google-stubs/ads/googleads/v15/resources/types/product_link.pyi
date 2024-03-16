from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.linked_product_type import (
    LinkedProductTypeEnum,
)

_M = TypeVar("_M")

class DataPartnerIdentifier(proto.Message):
    data_partner_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data_partner_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["data_partner_id"]
    ) -> bool: ...

class GoogleAdsIdentifier(proto.Message):
    customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer"]
    ) -> bool: ...

class MerchantCenterIdentifier(proto.Message):
    merchant_center_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        merchant_center_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["merchant_center_id"]
    ) -> bool: ...

class ProductLink(proto.Message):
    resource_name: str
    product_link_id: int
    type_: LinkedProductTypeEnum.LinkedProductType
    data_partner: DataPartnerIdentifier
    google_ads: GoogleAdsIdentifier
    merchant_center: MerchantCenterIdentifier
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        product_link_id: int = ...,
        type_: LinkedProductTypeEnum.LinkedProductType = ...,
        data_partner: DataPartnerIdentifier = ...,
        google_ads: GoogleAdsIdentifier = ...,
        merchant_center: MerchantCenterIdentifier = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "product_link_id",
            "type_",
            "data_partner",
            "google_ads",
            "merchant_center",
        ],
    ) -> bool: ...
