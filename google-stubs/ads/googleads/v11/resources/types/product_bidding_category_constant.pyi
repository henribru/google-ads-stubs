from typing import Any

import proto

from google.ads.googleads.v11.enums.types.product_bidding_category_level import (
    ProductBiddingCategoryLevelEnum,
)
from google.ads.googleads.v11.enums.types.product_bidding_category_status import (
    ProductBiddingCategoryStatusEnum,
)

class ProductBiddingCategoryConstant(proto.Message):
    resource_name: str
    id: int
    country_code: str
    product_bidding_category_constant_parent: str
    level: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    status: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus
    language_code: str
    localized_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        country_code: str = ...,
        product_bidding_category_constant_parent: str = ...,
        level: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel = ...,
        status: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus = ...,
        language_code: str = ...,
        localized_name: str = ...
    ) -> None: ...
