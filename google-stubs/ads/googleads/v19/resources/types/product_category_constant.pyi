from collections.abc import MutableSequence
from google.ads.googleads.v19.enums.types.product_category_state import ProductCategoryStateEnum
from google.ads.googleads.v19.enums.types.product_category_level import ProductCategoryLevelEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ProductCategoryConstant(proto.Message):
    class ProductCategoryLocalization(proto.Message):
        region_code: str
        language_code: str
        value: str
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, region_code: str = ..., language_code: str = ..., value: str = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["region_code", "language_code", "value"]) -> bool: ...
    resource_name: str
    category_id: int
    product_category_constant_parent: str
    level: ProductCategoryLevelEnum.ProductCategoryLevel
    state: ProductCategoryStateEnum.ProductCategoryState
    localizations: MutableSequence[ProductCategoryConstant.ProductCategoryLocalization]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., category_id: int = ..., product_category_constant_parent: str = ..., level: ProductCategoryLevelEnum.ProductCategoryLevel = ..., state: ProductCategoryStateEnum.ProductCategoryState = ..., localizations: MutableSequence[ProductCategoryConstant.ProductCategoryLocalization] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "category_id", "product_category_constant_parent", "level", "state", "localizations"]) -> bool: ...
