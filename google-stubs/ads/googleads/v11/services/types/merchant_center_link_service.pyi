from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v11.resources.types.merchant_center_link import (
    MerchantCenterLink,
)

class GetMerchantCenterLinkRequest(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class ListMerchantCenterLinksRequest(proto.Message):
    customer_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...
    ) -> None: ...

class ListMerchantCenterLinksResponse(proto.Message):
    merchant_center_links: list[MerchantCenterLink]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        merchant_center_links: list[MerchantCenterLink] = ...
    ) -> None: ...

class MerchantCenterLinkOperation(proto.Message):
    update_mask: FieldMask
    update: MerchantCenterLink
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: MerchantCenterLink = ...,
        remove: str = ...
    ) -> None: ...

class MutateMerchantCenterLinkRequest(proto.Message):
    customer_id: str
    operation: MerchantCenterLinkOperation
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: MerchantCenterLinkOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateMerchantCenterLinkResponse(proto.Message):
    result: MutateMerchantCenterLinkResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateMerchantCenterLinkResult = ...
    ) -> None: ...

class MutateMerchantCenterLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
