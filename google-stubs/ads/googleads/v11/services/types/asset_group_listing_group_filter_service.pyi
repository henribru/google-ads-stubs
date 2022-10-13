from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.asset_group_listing_group_filter import (
    AssetGroupListingGroupFilter,
)

class AssetGroupListingGroupFilterOperation(proto.Message):
    update_mask: FieldMask
    create: AssetGroupListingGroupFilter
    update: AssetGroupListingGroupFilter
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AssetGroupListingGroupFilter = ...,
        update: AssetGroupListingGroupFilter = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetGroupListingGroupFilterResult(proto.Message):
    resource_name: str
    asset_group_listing_group_filter: AssetGroupListingGroupFilter
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group_listing_group_filter: AssetGroupListingGroupFilter = ...
    ) -> None: ...

class MutateAssetGroupListingGroupFiltersRequest(proto.Message):
    customer_id: str
    operations: list[AssetGroupListingGroupFilterOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AssetGroupListingGroupFilterOperation] = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAssetGroupListingGroupFiltersResponse(proto.Message):
    results: list[MutateAssetGroupListingGroupFilterResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAssetGroupListingGroupFilterResult] = ...
    ) -> None: ...
