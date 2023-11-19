from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v13.resources.types.merchant_center_link import (
    MerchantCenterLink,
)

_M = TypeVar("_M")

class GetMerchantCenterLinkRequest(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class ListMerchantCenterLinksRequest(proto.Message):
    customer_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id"]) -> bool: ...  # type: ignore[override]

class ListMerchantCenterLinksResponse(proto.Message):
    merchant_center_links: MutableSequence[MerchantCenterLink]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        merchant_center_links: MutableSequence[MerchantCenterLink] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["merchant_center_links"]) -> bool: ...  # type: ignore[override]

class MerchantCenterLinkOperation(proto.Message):
    update_mask: FieldMask
    update: MerchantCenterLink
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        update: MerchantCenterLink = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "update", "remove"]) -> bool: ...  # type: ignore[override]

class MutateMerchantCenterLinkRequest(proto.Message):
    customer_id: str
    operation: MerchantCenterLinkOperation
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: MerchantCenterLinkOperation = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operation", "validate_only"]) -> bool: ...  # type: ignore[override]

class MutateMerchantCenterLinkResponse(proto.Message):
    result: MutateMerchantCenterLinkResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateMerchantCenterLinkResult = ...
    ) -> None: ...
    def __contains__(self, key: Literal["result"]) -> bool: ...  # type: ignore[override]

class MutateMerchantCenterLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]
