from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.product_link_invitation_status import (
    ProductLinkInvitationStatusEnum,
)
from google.ads.googleads.v16.resources.types.product_link_invitation import (
    ProductLinkInvitation,
)

_M = TypeVar("_M")

class CreateProductLinkInvitationRequest(proto.Message):
    customer_id: str
    product_link_invitation: ProductLinkInvitation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        product_link_invitation: ProductLinkInvitation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "product_link_invitation"]
    ) -> bool: ...

class CreateProductLinkInvitationResponse(proto.Message):
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

class RemoveProductLinkInvitationRequest(proto.Message):
    customer_id: str
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "resource_name"]
    ) -> bool: ...

class RemoveProductLinkInvitationResponse(proto.Message):
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
