from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.asset_group_listing_group_filter import (
    AssetGroupListingGroupFilter,
)

_M = TypeVar("_M")

class AssetGroupListingGroupFilterOperation(proto.Message):
    update_mask: FieldMask
    create: AssetGroupListingGroupFilter
    update: AssetGroupListingGroupFilter
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AssetGroupListingGroupFilter = ...,
        update: AssetGroupListingGroupFilter = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create", "update", "remove"]
    ) -> bool: ...

class MutateAssetGroupListingGroupFilterResult(proto.Message):
    resource_name: str
    asset_group_listing_group_filter: AssetGroupListingGroupFilter
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group_listing_group_filter: AssetGroupListingGroupFilter = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "asset_group_listing_group_filter"]
    ) -> bool: ...

class MutateAssetGroupListingGroupFiltersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetGroupListingGroupFilterOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AssetGroupListingGroupFilterOperation] = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id", "operations", "validate_only", "response_content_type"
        ],
    ) -> bool: ...

class MutateAssetGroupListingGroupFiltersResponse(proto.Message):
    results: MutableSequence[MutateAssetGroupListingGroupFilterResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAssetGroupListingGroupFilterResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["results"]
    ) -> bool: ...
