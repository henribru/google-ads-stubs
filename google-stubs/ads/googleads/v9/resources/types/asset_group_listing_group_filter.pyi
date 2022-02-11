from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    listing_group_filter_bidding_category_level as listing_group_filter_bidding_category_level,
    listing_group_filter_custom_attribute_index as listing_group_filter_custom_attribute_index,
    listing_group_filter_product_channel as listing_group_filter_product_channel,
    listing_group_filter_product_condition as listing_group_filter_product_condition,
    listing_group_filter_product_type_level as listing_group_filter_product_type_level,
    listing_group_filter_type_enum as listing_group_filter_type_enum,
    listing_group_filter_vertical as listing_group_filter_vertical,
)

__protobuf__: Any

class AssetGroupListingGroupFilter(proto.Message):
    resource_name: Any
    asset_group: Any
    id: Any
    type_: Any
    vertical: Any
    case_value: Any
    parent_listing_group_filter: Any

class ListingGroupFilterDimension(proto.Message):
    class ProductBiddingCategory(proto.Message):
        id: Any
        level: Any
    class ProductBrand(proto.Message):
        value: Any
    class ProductChannel(proto.Message):
        channel: Any
    class ProductCondition(proto.Message):
        condition: Any
    class ProductCustomAttribute(proto.Message):
        value: Any
        index: Any
    class ProductItemId(proto.Message):
        value: Any
    class ProductType(proto.Message):
        value: Any
        level: Any
    product_bidding_category: Any
    product_brand: Any
    product_channel: Any
    product_condition: Any
    product_custom_attribute: Any
    product_item_id: Any
    product_type: Any
