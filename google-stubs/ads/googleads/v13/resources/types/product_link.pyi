from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.linked_product_type import (
    LinkedProductTypeEnum,
)

_M = TypeVar("_M")

class DataPartnerIdentifier(proto.Message):
    data_partner_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        data_partner_id: int = ...
    ) -> None: ...

class GoogleAdsIdentifier(proto.Message):
    customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer: str = ...
    ) -> None: ...

class ProductLink(proto.Message):
    resource_name: str
    product_link_id: int
    type_: LinkedProductTypeEnum.LinkedProductType
    data_partner: DataPartnerIdentifier
    google_ads: GoogleAdsIdentifier
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        product_link_id: int = ...,
        type_: LinkedProductTypeEnum.LinkedProductType = ...,
        data_partner: DataPartnerIdentifier = ...,
        google_ads: GoogleAdsIdentifier = ...
    ) -> None: ...
