import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    listing_group_filter_bidding_category_level as listing_group_filter_bidding_category_level,
    listing_group_filter_custom_attribute_index as listing_group_filter_custom_attribute_index,
    listing_group_filter_product_channel as listing_group_filter_product_channel,
    listing_group_filter_product_condition as listing_group_filter_product_condition,
    listing_group_filter_product_type_level as listing_group_filter_product_type_level,
    listing_group_filter_type_enum as listing_group_filter_type_enum,
    listing_group_filter_vertical as listing_group_filter_vertical,
)

__protobuf__: Incomplete

class AssetGroupListingGroupFilter(proto.Message):
    resource_name: Incomplete
    asset_group: Incomplete
    id: Incomplete
    type_: Incomplete
    vertical: Incomplete
    case_value: Incomplete
    parent_listing_group_filter: Incomplete

class ListingGroupFilterDimension(proto.Message):
    class ProductBiddingCategory(proto.Message):
        id: Incomplete
        level: Incomplete

    class ProductBrand(proto.Message):
        value: Incomplete

    class ProductChannel(proto.Message):
        channel: Incomplete

    class ProductCondition(proto.Message):
        condition: Incomplete

    class ProductCustomAttribute(proto.Message):
        value: Incomplete
        index: Incomplete

    class ProductItemId(proto.Message):
        value: Incomplete

    class ProductType(proto.Message):
        value: Incomplete
        level: Incomplete
    product_bidding_category: Incomplete
    product_brand: Incomplete
    product_channel: Incomplete
    product_condition: Incomplete
    product_custom_attribute: Incomplete
    product_item_id: Incomplete
    product_type: Incomplete
