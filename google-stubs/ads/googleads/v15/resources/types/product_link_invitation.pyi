from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        hotel_center_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["hotel_center_id"]
    ) -> bool: ...

class MerchantCenterLinkInvitationIdentifier(proto.Message):
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
        merchant_center: MerchantCenterLinkInvitationIdentifier = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "product_link_invitation_id",
            "status",
            "type_",
            "hotel_center",
            "merchant_center",
        ],
    ) -> bool: ...
