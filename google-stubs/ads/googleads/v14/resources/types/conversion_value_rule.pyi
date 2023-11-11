from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.conversion_value_rule_status import (
    ConversionValueRuleStatusEnum,
)
from google.ads.googleads.v14.enums.types.value_rule_device_type import (
    ValueRuleDeviceTypeEnum,
)
from google.ads.googleads.v14.enums.types.value_rule_geo_location_match_type import (
    ValueRuleGeoLocationMatchTypeEnum,
)
from google.ads.googleads.v14.enums.types.value_rule_operation import (
    ValueRuleOperationEnum,
)

_M = TypeVar("_M")

class ConversionValueRule(proto.Message):
    class ValueRuleAction(proto.Message):
        operation: ValueRuleOperationEnum.ValueRuleOperation
        value: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            operation: ValueRuleOperationEnum.ValueRuleOperation = ...,
            value: float = ...
        ) -> None: ...

    class ValueRuleAudienceCondition(proto.Message):
        user_lists: MutableSequence[str]
        user_interests: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            user_lists: MutableSequence[str] = ...,
            user_interests: MutableSequence[str] = ...
        ) -> None: ...

    class ValueRuleDeviceCondition(proto.Message):
        device_types: MutableSequence[ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            device_types: MutableSequence[
                ValueRuleDeviceTypeEnum.ValueRuleDeviceType
            ] = ...
        ) -> None: ...

    class ValueRuleGeoLocationCondition(proto.Message):
        excluded_geo_target_constants: MutableSequence[str]
        excluded_geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
        geo_target_constants: MutableSequence[str]
        geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            excluded_geo_target_constants: MutableSequence[str] = ...,
            excluded_geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType = ...,
            geo_target_constants: MutableSequence[str] = ...,
            geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType = ...
        ) -> None: ...
    resource_name: str
    id: int
    action: ConversionValueRule.ValueRuleAction
    geo_location_condition: ConversionValueRule.ValueRuleGeoLocationCondition
    device_condition: ConversionValueRule.ValueRuleDeviceCondition
    audience_condition: ConversionValueRule.ValueRuleAudienceCondition
    owner_customer: str
    status: ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        action: ConversionValueRule.ValueRuleAction = ...,
        geo_location_condition: ConversionValueRule.ValueRuleGeoLocationCondition = ...,
        device_condition: ConversionValueRule.ValueRuleDeviceCondition = ...,
        audience_condition: ConversionValueRule.ValueRuleAudienceCondition = ...,
        owner_customer: str = ...,
        status: ConversionValueRuleStatusEnum.ConversionValueRuleStatus = ...
    ) -> None: ...
