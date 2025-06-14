from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.product_status import ProductStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.product_availability import ProductAvailabilityEnum
from google.ads.googleads.v18.enums.types.product_condition import ProductConditionEnum
from google.ads.googleads.v18.enums.types.product_channel_exclusivity import ProductChannelExclusivityEnum
from google.ads.googleads.v18.enums.types.product_channel import ProductChannelEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.product_issue_severity import ProductIssueSeverityEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ShoppingProduct(proto.Message):
    class ProductIssue(proto.Message):
        error_code: str
        ads_severity: ProductIssueSeverityEnum.ProductIssueSeverity
        attribute_name: str
        description: str
        detail: str
        documentation: str
        affected_regions: MutableSequence[str]
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, error_code: str = ..., ads_severity: ProductIssueSeverityEnum.ProductIssueSeverity = ..., attribute_name: str = ..., description: str = ..., detail: str = ..., documentation: str = ..., affected_regions: MutableSequence[str] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["error_code", "ads_severity", "attribute_name", "description", "detail", "documentation", "affected_regions"]) -> bool: ...
    resource_name: str
    merchant_center_id: int
    channel: ProductChannelEnum.ProductChannel
    language_code: str
    feed_label: str
    item_id: str
    multi_client_account_id: int
    title: str
    brand: str
    price_micros: int
    currency_code: str
    channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity
    condition: ProductConditionEnum.ProductCondition
    availability: ProductAvailabilityEnum.ProductAvailability
    target_countries: MutableSequence[str]
    custom_attribute0: str
    custom_attribute1: str
    custom_attribute2: str
    custom_attribute3: str
    custom_attribute4: str
    category_level1: str
    category_level2: str
    category_level3: str
    category_level4: str
    category_level5: str
    product_type_level1: str
    product_type_level2: str
    product_type_level3: str
    product_type_level4: str
    product_type_level5: str
    effective_max_cpc_micros: int
    status: ProductStatusEnum.ProductStatus
    issues: MutableSequence[ShoppingProduct.ProductIssue]
    campaign: str
    ad_group: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., merchant_center_id: int = ..., channel: ProductChannelEnum.ProductChannel = ..., language_code: str = ..., feed_label: str = ..., item_id: str = ..., multi_client_account_id: int = ..., title: str = ..., brand: str = ..., price_micros: int = ..., currency_code: str = ..., channel_exclusivity: ProductChannelExclusivityEnum.ProductChannelExclusivity = ..., condition: ProductConditionEnum.ProductCondition = ..., availability: ProductAvailabilityEnum.ProductAvailability = ..., target_countries: MutableSequence[str] = ..., custom_attribute0: str = ..., custom_attribute1: str = ..., custom_attribute2: str = ..., custom_attribute3: str = ..., custom_attribute4: str = ..., category_level1: str = ..., category_level2: str = ..., category_level3: str = ..., category_level4: str = ..., category_level5: str = ..., product_type_level1: str = ..., product_type_level2: str = ..., product_type_level3: str = ..., product_type_level4: str = ..., product_type_level5: str = ..., effective_max_cpc_micros: int = ..., status: ProductStatusEnum.ProductStatus = ..., issues: MutableSequence[ShoppingProduct.ProductIssue] = ..., campaign: str = ..., ad_group: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "merchant_center_id", "channel", "language_code", "feed_label", "item_id", "multi_client_account_id", "title", "brand", "price_micros", "currency_code", "channel_exclusivity", "condition", "availability", "target_countries", "custom_attribute0", "custom_attribute1", "custom_attribute2", "custom_attribute3", "custom_attribute4", "category_level1", "category_level2", "category_level3", "category_level4", "category_level5", "product_type_level1", "product_type_level2", "product_type_level3", "product_type_level4", "product_type_level5", "effective_max_cpc_micros", "status", "issues", "campaign", "ad_group"]) -> bool: ...
