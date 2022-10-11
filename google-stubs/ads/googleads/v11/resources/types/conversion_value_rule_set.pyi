import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    conversion_action_category as conversion_action_category,
    conversion_value_rule_set_status as conversion_value_rule_set_status,
    value_rule_set_attachment_type as value_rule_set_attachment_type,
    value_rule_set_dimension as value_rule_set_dimension,
)

__protobuf__: Incomplete

class ConversionValueRuleSet(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    conversion_value_rules: Incomplete
    dimensions: Incomplete
    owner_customer: Incomplete
    attachment_type: Incomplete
    campaign: Incomplete
    status: Incomplete
    conversion_action_categories: Incomplete
