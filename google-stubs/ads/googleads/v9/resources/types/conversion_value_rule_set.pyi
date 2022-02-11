from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    conversion_value_rule_set_status as conversion_value_rule_set_status,
    value_rule_set_attachment_type as value_rule_set_attachment_type,
    value_rule_set_dimension as value_rule_set_dimension,
)

__protobuf__: Any

class ConversionValueRuleSet(proto.Message):
    resource_name: Any
    id: Any
    conversion_value_rules: Any
    dimensions: Any
    owner_customer: Any
    attachment_type: Any
    campaign: Any
    status: Any
