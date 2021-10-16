from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    conversion_value_rule_status as conversion_value_rule_status,
    value_rule_device_type as value_rule_device_type,
    value_rule_geo_location_match_type as value_rule_geo_location_match_type,
    value_rule_operation as value_rule_operation,
)

__protobuf__: Any

class ConversionValueRule(proto.Message):
    class ValueRuleAction(proto.Message):
        operation: Any
        value: Any
    class ValueRuleGeoLocationCondition(proto.Message):
        excluded_geo_target_constants: Any
        excluded_geo_match_type: Any
        geo_target_constants: Any
        geo_match_type: Any
    class ValueRuleAudienceCondition(proto.Message):
        user_lists: Any
        user_interests: Any
    class ValueRuleDeviceCondition(proto.Message):
        device_types: Any
    resource_name: Any
    id: Any
    action: Any
    geo_location_condition: Any
    device_condition: Any
    audience_condition: Any
    owner_customer: Any
    status: Any
