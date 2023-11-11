from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v15.enums.types.product_category_level import (
    ProductCategoryLevelEnum,
)
from google.ads.googleads.v15.enums.types.product_category_state import (
    ProductCategoryStateEnum,
)

class ProductCategoryConstant(proto.Message):
    class ProductCategoryLocalization(proto.Message):
        region_code: str
        language_code: str
        value: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            region_code: str = ...,
            language_code: str = ...,
            value: str = ...
        ) -> None: ...
    resource_name: str
    category_id: int
    product_category_constant_parent: str
    level: ProductCategoryLevelEnum.ProductCategoryLevel
    state: ProductCategoryStateEnum.ProductCategoryState
    localizations: MutableSequence[ProductCategoryConstant.ProductCategoryLocalization]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        category_id: int = ...,
        product_category_constant_parent: str = ...,
        level: ProductCategoryLevelEnum.ProductCategoryLevel = ...,
        state: ProductCategoryStateEnum.ProductCategoryState = ...,
        localizations: MutableSequence[
            ProductCategoryConstant.ProductCategoryLocalization
        ] = ...
    ) -> None: ...
