import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import product_availability, product_channel, product_channel_exclusivity, product_condition, product_issue_severity, product_status
from typing import MutableSequence

__protobuf__: Incomplete

class ShoppingProduct(proto.Message):
    class ProductIssue(proto.Message):
        error_code: str
        ads_severity: product_issue_severity.ProductIssueSeverityEnum.ProductIssueSeverity
        attribute_name: str
        description: str
        detail: str
        documentation: str
        affected_regions: MutableSequence[str]
    resource_name: str
    merchant_center_id: int
    channel: product_channel.ProductChannelEnum.ProductChannel
    language_code: str
    feed_label: str
    item_id: str
    multi_client_account_id: int
    title: str
    brand: str
    price_micros: int
    currency_code: str
    channel_exclusivity: product_channel_exclusivity.ProductChannelExclusivityEnum.ProductChannelExclusivity
    condition: product_condition.ProductConditionEnum.ProductCondition
    availability: product_availability.ProductAvailabilityEnum.ProductAvailability
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
    status: product_status.ProductStatusEnum.ProductStatus
    issues: MutableSequence[ProductIssue]
    campaign: str
    ad_group: str
