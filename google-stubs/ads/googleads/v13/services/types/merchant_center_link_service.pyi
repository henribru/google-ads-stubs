from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

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

class ListMerchantCenterLinksRequest(proto.Message):
    customer_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...
    ) -> None: ...

class ListMerchantCenterLinksResponse(proto.Message):
    merchant_center_links: MutableSequence[MerchantCenterLink]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        merchant_center_links: MutableSequence[MerchantCenterLink] = ...
    ) -> None: ...

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

class MutateMerchantCenterLinkResponse(proto.Message):
    result: MutateMerchantCenterLinkResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateMerchantCenterLinkResult = ...
    ) -> None: ...

class MutateMerchantCenterLinkResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
