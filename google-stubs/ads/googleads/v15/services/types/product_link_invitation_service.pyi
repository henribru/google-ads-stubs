from typing import Any

import proto

from google.ads.googleads.v15.enums.types.product_link_invitation_status import (
    ProductLinkInvitationStatusEnum,
)

class UpdateProductLinkInvitationRequest(proto.Message):
    customer_id: str
    product_link_invitation_status: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        product_link_invitation_status: ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus = ...,
        resource_name: str = ...
    ) -> None: ...

class UpdateProductLinkInvitationResponse(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
