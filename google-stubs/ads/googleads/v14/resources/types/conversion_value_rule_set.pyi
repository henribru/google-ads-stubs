from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v14.enums.types.conversion_value_rule_set_status import (
    ConversionValueRuleSetStatusEnum,
)
from google.ads.googleads.v14.enums.types.value_rule_set_attachment_type import (
    ValueRuleSetAttachmentTypeEnum,
)
from google.ads.googleads.v14.enums.types.value_rule_set_dimension import (
    ValueRuleSetDimensionEnum,
)

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
