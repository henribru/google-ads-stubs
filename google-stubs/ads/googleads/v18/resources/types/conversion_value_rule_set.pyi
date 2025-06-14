import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import conversion_action_category, conversion_value_rule_set_status, value_rule_set_attachment_type, value_rule_set_dimension
from typing import MutableSequence

__protobuf__: Incomplete

class ConversionValueRuleSet(proto.Message):
    resource_name: str
    id: int
    conversion_value_rules: MutableSequence[str]
    dimensions: MutableSequence[value_rule_set_dimension.ValueRuleSetDimensionEnum.ValueRuleSetDimension]
    owner_customer: str
    attachment_type: value_rule_set_attachment_type.ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    campaign: str
    status: conversion_value_rule_set_status.ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    conversion_action_categories: MutableSequence[conversion_action_category.ConversionActionCategoryEnum.ConversionActionCategory]
