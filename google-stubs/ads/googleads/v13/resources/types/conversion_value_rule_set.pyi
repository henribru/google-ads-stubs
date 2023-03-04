from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v13.enums.types.conversion_value_rule_set_status import (
    ConversionValueRuleSetStatusEnum,
)
from google.ads.googleads.v13.enums.types.value_rule_set_attachment_type import (
    ValueRuleSetAttachmentTypeEnum,
)
from google.ads.googleads.v13.enums.types.value_rule_set_dimension import (
    ValueRuleSetDimensionEnum,
)

class ConversionValueRuleSet(proto.Message):
    resource_name: str
    id: int
    conversion_value_rules: MutableSequence[str]
    dimensions: MutableSequence[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
    owner_customer: str
    attachment_type: ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    campaign: str
    status: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    conversion_action_categories: MutableSequence[
        ConversionActionCategoryEnum.ConversionActionCategory
    ]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        conversion_value_rules: MutableSequence[str] = ...,
        dimensions: MutableSequence[
            ValueRuleSetDimensionEnum.ValueRuleSetDimension
        ] = ...,
        owner_customer: str = ...,
        attachment_type: ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType = ...,
        campaign: str = ...,
        status: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus = ...,
        conversion_action_categories: MutableSequence[
            ConversionActionCategoryEnum.ConversionActionCategory
        ] = ...
    ) -> None: ...
