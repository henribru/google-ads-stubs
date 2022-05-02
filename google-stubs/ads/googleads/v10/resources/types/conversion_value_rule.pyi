import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    conversion_value_rule_status as conversion_value_rule_status,
    value_rule_device_type as value_rule_device_type,
    value_rule_geo_location_match_type as value_rule_geo_location_match_type,
    value_rule_operation as value_rule_operation,
)

__protobuf__: Incomplete

class ConversionValueRule(proto.Message):
    class ValueRuleAction(proto.Message):
        operation: Incomplete
        value: Incomplete

    class ValueRuleGeoLocationCondition(proto.Message):
        excluded_geo_target_constants: Incomplete
        excluded_geo_match_type: Incomplete
        geo_target_constants: Incomplete
        geo_match_type: Incomplete

    class ValueRuleDeviceCondition(proto.Message):
        device_types: Incomplete

    class ValueRuleAudienceCondition(proto.Message):
        user_lists: Incomplete
        user_interests: Incomplete
    resource_name: Incomplete
    id: Incomplete
    action: Incomplete
    geo_location_condition: Incomplete
    device_condition: Incomplete
    audience_condition: Incomplete
    owner_customer: Incomplete
    status: Incomplete
