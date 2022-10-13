from typing import Any

import proto

from google.ads.googleads.v11.enums.types.listing_group_filter_bidding_category_level import (
    ListingGroupFilterBiddingCategoryLevelEnum,
)
from google.ads.googleads.v11.enums.types.listing_group_filter_custom_attribute_index import (
    ListingGroupFilterCustomAttributeIndexEnum,
)
from google.ads.googleads.v11.enums.types.listing_group_filter_product_channel import (
    ListingGroupFilterProductChannelEnum,
)
from google.ads.googleads.v11.enums.types.listing_group_filter_product_condition import (
    ListingGroupFilterProductConditionEnum,
)
from google.ads.googleads.v11.enums.types.listing_group_filter_product_type_level import (
    ListingGroupFilterProductTypeLevelEnum,
)
from google.ads.googleads.v11.enums.types.listing_group_filter_type_enum import (
    ListingGroupFilterTypeEnum,
)
from google.ads.googleads.v11.enums.types.listing_group_filter_vertical import (
    ListingGroupFilterVerticalEnum,
)

class AssetGroupListingGroupFilter(proto.Message):
    resource_name: str
    asset_group: str
    id: int
    type_: ListingGroupFilterTypeEnum.ListingGroupFilterType
    vertical: ListingGroupFilterVerticalEnum.ListingGroupFilterVertical
    case_value: ListingGroupFilterDimension
    parent_listing_group_filter: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group: str = ...,
        id: int = ...,
        type_: ListingGroupFilterTypeEnum.ListingGroupFilterType = ...,
        vertical: ListingGroupFilterVerticalEnum.ListingGroupFilterVertical = ...,
        case_value: ListingGroupFilterDimension = ...,
        parent_listing_group_filter: str = ...
    ) -> None: ...

class ListingGroupFilterDimension(proto.Message):
    class ProductBiddingCategory(proto.Message):
        id: int
        level: ListingGroupFilterBiddingCategoryLevelEnum.ListingGroupFilterBiddingCategoryLevel
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            id: int = ...,
            level: ListingGroupFilterBiddingCategoryLevelEnum.ListingGroupFilterBiddingCategoryLevel = ...
        ) -> None: ...

    class ProductBrand(proto.Message):
        value: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            value: str = ...
        ) -> None: ...

    class ProductChannel(proto.Message):
        channel: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            channel: ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel = ...
        ) -> None: ...

    class ProductCondition(proto.Message):
        condition: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            condition: ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition = ...
        ) -> None: ...

    class ProductCustomAttribute(proto.Message):
        value: str
        index: ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            value: str = ...,
            index: ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex = ...
        ) -> None: ...

    class ProductItemId(proto.Message):
        value: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            value: str = ...
        ) -> None: ...

    class ProductType(proto.Message):
        value: str
        level: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            value: str = ...,
            level: ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel = ...
        ) -> None: ...
    product_bidding_category: ListingGroupFilterDimension.ProductBiddingCategory
    product_brand: ListingGroupFilterDimension.ProductBrand
    product_channel: ListingGroupFilterDimension.ProductChannel
    product_condition: ListingGroupFilterDimension.ProductCondition
    product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute
    product_item_id: ListingGroupFilterDimension.ProductItemId
    product_type: ListingGroupFilterDimension.ProductType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        product_bidding_category: ListingGroupFilterDimension.ProductBiddingCategory = ...,
        product_brand: ListingGroupFilterDimension.ProductBrand = ...,
        product_channel: ListingGroupFilterDimension.ProductChannel = ...,
        product_condition: ListingGroupFilterDimension.ProductCondition = ...,
        product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute = ...,
        product_item_id: ListingGroupFilterDimension.ProductItemId = ...,
        product_type: ListingGroupFilterDimension.ProductType = ...
    ) -> None: ...
