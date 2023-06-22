from typing import Any

import proto

from google.ads.googleads.v14.resources.types.product_link import ProductLink

class CreateProductLinkRequest(proto.Message):
    customer_id: str
    product_link: ProductLink
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        product_link: ProductLink = ...
    ) -> None: ...

class CreateProductLinkResponse(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class RemoveProductLinkRequest(proto.Message):
    customer_id: str
    resource_name: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        resource_name: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class RemoveProductLinkResponse(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
