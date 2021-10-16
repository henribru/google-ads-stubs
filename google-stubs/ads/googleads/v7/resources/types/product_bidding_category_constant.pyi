from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    product_bidding_category_level as product_bidding_category_level,
    product_bidding_category_status as product_bidding_category_status,
)

__protobuf__: Any

class ProductBiddingCategoryConstant(proto.Message):
    resource_name: Any
    id: Any
    country_code: Any
    product_bidding_category_constant_parent: Any
    level: Any
    status: Any
    language_code: Any
    localized_name: Any
