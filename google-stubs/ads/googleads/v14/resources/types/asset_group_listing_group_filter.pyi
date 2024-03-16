from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.listing_group_filter_bidding_category_level import (
    ListingGroupFilterBiddingCategoryLevelEnum,
)
from google.ads.googleads.v14.enums.types.listing_group_filter_custom_attribute_index import (
    ListingGroupFilterCustomAttributeIndexEnum,
)
from google.ads.googleads.v14.enums.types.listing_group_filter_product_channel import (
    ListingGroupFilterProductChannelEnum,
)
from google.ads.googleads.v14.enums.types.listing_group_filter_product_condition import (
    ListingGroupFilterProductConditionEnum,
)
from google.ads.googleads.v14.enums.types.listing_group_filter_product_type_level import (
    ListingGroupFilterProductTypeLevelEnum,
)
from google.ads.googleads.v14.enums.types.listing_group_filter_type_enum import (
    ListingGroupFilterTypeEnum,
)
from google.ads.googleads.v14.enums.types.listing_group_filter_vertical import (
    ListingGroupFilterVerticalEnum,
)

_M = TypeVar("_M")

class AssetGroupListingGroupFilter(proto.Message):
    resource_name: str
    asset_group: str
    id: int
    type_: ListingGroupFilterTypeEnum.ListingGroupFilterType
    vertical: ListingGroupFilterVerticalEnum.ListingGroupFilterVertical
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
        vertical: ListingGroupFilterVerticalEnum.ListingGroupFilterVertical = ...,
        case_value: ListingGroupFilterDimension = ...,
        parent_listing_group_filter: str = ...,
        path: ListingGroupFilterDimensionPath = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "asset_group",
            "id",
            "type_",
            "vertical",
            "case_value",
            "parent_listing_group_filter",
            "path",
        ],
    ) -> bool: ...

class ListingGroupFilterDimension(proto.Message):
    class ProductBiddingCategory(proto.Message):
        id: int
        level: ListingGroupFilterBiddingCategoryLevelEnum.ListingGroupFilterBiddingCategoryLevel
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            id: int = ...,
            level: ListingGroupFilterBiddingCategoryLevelEnum.ListingGroupFilterBiddingCategoryLevel = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["id", "level"]
        ) -> bool: ...

    class ProductBrand(proto.Message):
        value: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["value"]
        ) -> bool: ...

    class ProductChannel(proto.Message):
        channel: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            channel: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["channel"]
        ) -> bool: ...

    class ProductCondition(proto.Message):
        condition: (
            ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
        )
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            condition: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["condition"]
        ) -> bool: ...

    class ProductCustomAttribute(proto.Message):
        value: str
        index: ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...,
            index: ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["value", "index"]
        ) -> bool: ...

    class ProductItemId(proto.Message):
        value: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["value"]
        ) -> bool: ...

    class ProductType(proto.Message):
        value: str
        level: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value: str = ...,
            level: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["value", "level"]
        ) -> bool: ...

    product_bidding_category: ListingGroupFilterDimension.ProductBiddingCategory
    product_brand: ListingGroupFilterDimension.ProductBrand
    product_channel: ListingGroupFilterDimension.ProductChannel
    product_condition: ListingGroupFilterDimension.ProductCondition
    product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute
    product_item_id: ListingGroupFilterDimension.ProductItemId
    product_type: ListingGroupFilterDimension.ProductType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        product_bidding_category: ListingGroupFilterDimension.ProductBiddingCategory = ...,
        product_brand: ListingGroupFilterDimension.ProductBrand = ...,
        product_channel: ListingGroupFilterDimension.ProductChannel = ...,
        product_condition: ListingGroupFilterDimension.ProductCondition = ...,
        product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute = ...,
        product_item_id: ListingGroupFilterDimension.ProductItemId = ...,
        product_type: ListingGroupFilterDimension.ProductType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "product_bidding_category",
            "product_brand",
            "product_channel",
            "product_condition",
            "product_custom_attribute",
            "product_item_id",
            "product_type",
        ],
    ) -> bool: ...

class ListingGroupFilterDimensionPath(proto.Message):
    dimensions: MutableSequence[ListingGroupFilterDimension]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dimensions: MutableSequence[ListingGroupFilterDimension] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dimensions"]
    ) -> bool: ...
