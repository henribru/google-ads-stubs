from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.conversion_action_category import ConversionActionCategoryEnum
from google.ads.googleads.v22.enums.types.conversion_value_rule_set_status import ConversionValueRuleSetStatusEnum
from google.ads.googleads.v22.enums.types.value_rule_set_attachment_type import ValueRuleSetAttachmentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.value_rule_set_dimension import ValueRuleSetDimensionEnum
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    conversion_action_categories: MutableSequence[ConversionActionCategoryEnum.ConversionActionCategory]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., conversion_value_rules: MutableSequence[str] = ..., dimensions: MutableSequence[ValueRuleSetDimensionEnum.ValueRuleSetDimension] = ..., owner_customer: str = ..., attachment_type: ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType = ..., campaign: str = ..., status: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus = ..., conversion_action_categories: MutableSequence[ConversionActionCategoryEnum.ConversionActionCategory] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "conversion_value_rules", "dimensions", "owner_customer", "attachment_type", "campaign", "status", "conversion_action_categories"]) -> bool: ...
