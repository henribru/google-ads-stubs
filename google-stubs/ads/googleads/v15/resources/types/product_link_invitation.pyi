from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.linked_product_type import (
    LinkedProductTypeEnum,
)
from google.ads.googleads.v15.enums.types.product_link_invitation_status import (
    ProductLinkInvitationStatusEnum,
)

_M = TypeVar("_M")

class HotelCenterLinkInvitationIdentifier(proto.Message):
    hotel_center_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        hotel_center_id: int = ...
    ) -> None: ...

class MerchantCenterLinkInvitationIdentifier(proto.Message):
    merchant_center_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        merchant_center_id: int = ...
    ) -> None: ...

class ProductLinkInvitation(proto.Message):
    resource_name: str
    product_link_invitation_id: int
    status: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    type_: LinkedProductTypeEnum.LinkedProductType
    hotel_center: HotelCenterLinkInvitationIdentifier
    merchant_center: MerchantCenterLinkInvitationIdentifier
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        product_link_invitation_id: int = ...,
        status: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus = ...,
        type_: LinkedProductTypeEnum.LinkedProductType = ...,
        hotel_center: HotelCenterLinkInvitationIdentifier = ...,
        merchant_center: MerchantCenterLinkInvitationIdentifier = ...
    ) -> None: ...
