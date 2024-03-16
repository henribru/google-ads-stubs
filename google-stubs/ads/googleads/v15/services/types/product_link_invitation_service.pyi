from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.product_link_invitation_status import (
    ProductLinkInvitationStatusEnum,
)

_M = TypeVar("_M")

class UpdateProductLinkInvitationRequest(proto.Message):
    customer_id: str
    product_link_invitation_status: (
        ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    )
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        product_link_invitation_status: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus = ...,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["customer_id", "product_link_invitation_status", "resource_name"],
    ) -> bool: ...

class UpdateProductLinkInvitationResponse(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name"]
    ) -> bool: ...
