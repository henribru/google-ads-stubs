import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import product_category_level, product_category_state
from typing import MutableSequence

__protobuf__: Incomplete

class ProductCategoryConstant(proto.Message):
    class ProductCategoryLocalization(proto.Message):
        region_code: str
        language_code: str
        value: str
    resource_name: str
    category_id: int
    product_category_constant_parent: str
    level: product_category_level.ProductCategoryLevelEnum.ProductCategoryLevel
    state: product_category_state.ProductCategoryStateEnum.ProductCategoryState
    localizations: MutableSequence[ProductCategoryLocalization]
