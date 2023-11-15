from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.product_bidding_category_level import (
    ProductBiddingCategoryLevelEnum,
)
from google.ads.googleads.v13.enums.types.product_bidding_category_status import (
    ProductBiddingCategoryStatusEnum,
)

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        country_code: str = ...,
        product_bidding_category_constant_parent: str = ...,
        level: ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel = ...,
        status: ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus = ...,
        language_code: str = ...,
        localized_name: str = ...
    ) -> None: ...
