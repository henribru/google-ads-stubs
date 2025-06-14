import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import listing_group_filter_custom_attribute_index, listing_group_filter_listing_source, listing_group_filter_product_category_level, listing_group_filter_product_channel, listing_group_filter_product_condition, listing_group_filter_product_type_level, listing_group_filter_type_enum
from typing import MutableSequence

__protobuf__: Incomplete

class AssetGroupListingGroupFilter(proto.Message):
    resource_name: str
    asset_group: str
    id: int
    type_: listing_group_filter_type_enum.ListingGroupFilterTypeEnum.ListingGroupFilterType
    listing_source: listing_group_filter_listing_source.ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    case_value: ListingGroupFilterDimension
    parent_listing_group_filter: str
    path: ListingGroupFilterDimensionPath

class ListingGroupFilterDimensionPath(proto.Message):
    dimensions: MutableSequence['ListingGroupFilterDimension']

class ListingGroupFilterDimension(proto.Message):
    class ProductCategory(proto.Message):
        category_id: int
        level: listing_group_filter_product_category_level.ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    class ProductBrand(proto.Message):
        value: str
    class ProductChannel(proto.Message):
        channel: listing_group_filter_product_channel.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
    class ProductCondition(proto.Message):
        condition: listing_group_filter_product_condition.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    class ProductCustomAttribute(proto.Message):
        value: str
        index: listing_group_filter_custom_attribute_index.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
    class ProductItemId(proto.Message):
        value: str
    class ProductType(proto.Message):
        value: str
        level: listing_group_filter_product_type_level.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    class Webpage(proto.Message):
        conditions: MutableSequence['ListingGroupFilterDimension.WebpageCondition']
    class WebpageCondition(proto.Message):
        custom_label: str
        url_contains: str
    product_category: ProductCategory
    product_brand: ProductBrand
    product_channel: ProductChannel
    product_condition: ProductCondition
    product_custom_attribute: ProductCustomAttribute
    product_item_id: ProductItemId
    product_type: ProductType
    webpage: Webpage
