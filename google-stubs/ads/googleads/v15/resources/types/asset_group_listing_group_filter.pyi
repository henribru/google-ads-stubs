from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.listing_group_filter_custom_attribute_index import (
    ListingGroupFilterCustomAttributeIndexEnum,
)
from google.ads.googleads.v15.enums.types.listing_group_filter_listing_source import (
    ListingGroupFilterListingSourceEnum,
)
from google.ads.googleads.v15.enums.types.listing_group_filter_product_category_level import (
    ListingGroupFilterProductCategoryLevelEnum,
)
from google.ads.googleads.v15.enums.types.listing_group_filter_product_channel import (
    ListingGroupFilterProductChannelEnum,
)
from google.ads.googleads.v15.enums.types.listing_group_filter_product_condition import (
    ListingGroupFilterProductConditionEnum,
)
from google.ads.googleads.v15.enums.types.listing_group_filter_product_type_level import (
    ListingGroupFilterProductTypeLevelEnum,
)
from google.ads.googleads.v15.enums.types.listing_group_filter_type_enum import (
    ListingGroupFilterTypeEnum,
)

_M = TypeVar("_M")

class AssetGroupListingGroupFilter(proto.Message):
    resource_name: str
    asset_group: str
    id: int
    type_: ListingGroupFilterTypeEnum.ListingGroupFilterType
    listing_source: ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    case_value: ListingGroupFilterDimension
    parent_listing_group_filter: str
    path: ListingGroupFilterDimensionPath
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group: str = ...,
        id: int = ...,
        type_: ListingGroupFilterTypeEnum.ListingGroupFilterType = ...,
        listing_source: ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource = ...,
        case_value: ListingGroupFilterDimension = ...,
        parent_listing_group_filter: str = ...,
        path: ListingGroupFilterDimensionPath = ...
    ) -> None: ...

class ListingGroupFilterDimension(proto.Message):
    class ProductBrand(proto.Message):
        value: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...
        ) -> None: ...

    class ProductCategory(proto.Message):
        category_id: int
        level: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            category_id: int = ...,
            level: ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel = ...
        ) -> None: ...

    class ProductChannel(proto.Message):
        channel: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            channel: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel = ...
        ) -> None: ...

    class ProductCondition(proto.Message):
        condition: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            condition: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition = ...
        ) -> None: ...

    class ProductCustomAttribute(proto.Message):
        value: str
        index: ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...,
            index: ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex = ...
        ) -> None: ...

    class ProductItemId(proto.Message):
        value: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...
        ) -> None: ...

    class ProductType(proto.Message):
        value: str
        level: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...,
            level: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel = ...
        ) -> None: ...

    class Webpage(proto.Message):
        conditions: MutableSequence[ListingGroupFilterDimension.WebpageCondition]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            conditions: MutableSequence[
                ListingGroupFilterDimension.WebpageCondition
            ] = ...
        ) -> None: ...

    class WebpageCondition(proto.Message):
        custom_label: str
        url_contains: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            custom_label: str = ...,
            url_contains: str = ...
        ) -> None: ...
    product_category: ListingGroupFilterDimension.ProductCategory
    product_brand: ListingGroupFilterDimension.ProductBrand
    product_channel: ListingGroupFilterDimension.ProductChannel
    product_condition: ListingGroupFilterDimension.ProductCondition
    product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute
    product_item_id: ListingGroupFilterDimension.ProductItemId
    product_type: ListingGroupFilterDimension.ProductType
    webpage: ListingGroupFilterDimension.Webpage
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        product_category: ListingGroupFilterDimension.ProductCategory = ...,
        product_brand: ListingGroupFilterDimension.ProductBrand = ...,
        product_channel: ListingGroupFilterDimension.ProductChannel = ...,
        product_condition: ListingGroupFilterDimension.ProductCondition = ...,
        product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute = ...,
        product_item_id: ListingGroupFilterDimension.ProductItemId = ...,
        product_type: ListingGroupFilterDimension.ProductType = ...,
        webpage: ListingGroupFilterDimension.Webpage = ...
    ) -> None: ...

class ListingGroupFilterDimensionPath(proto.Message):
    dimensions: MutableSequence[ListingGroupFilterDimension]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimensions: MutableSequence[ListingGroupFilterDimension] = ...
    ) -> None: ...
