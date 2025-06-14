import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import conversion_value_rule_status, value_rule_device_type, value_rule_geo_location_match_type, value_rule_operation
from typing import MutableSequence

__protobuf__: Incomplete

class ConversionValueRule(proto.Message):
    class ValueRuleAction(proto.Message):
        operation: value_rule_operation.ValueRuleOperationEnum.ValueRuleOperation
        value: float
    class ValueRuleGeoLocationCondition(proto.Message):
        excluded_geo_target_constants: MutableSequence[str]
        excluded_geo_match_type: value_rule_geo_location_match_type.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
        geo_target_constants: MutableSequence[str]
        geo_match_type: value_rule_geo_location_match_type.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
    class ValueRuleDeviceCondition(proto.Message):
        device_types: MutableSequence[value_rule_device_type.ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
    class ValueRuleAudienceCondition(proto.Message):
        user_lists: MutableSequence[str]
        user_interests: MutableSequence[str]
    class ValueRuleItineraryCondition(proto.Message):
        advance_booking_window: ConversionValueRule.ValueRuleItineraryAdvanceBookingWindow
        travel_length: ConversionValueRule.ValueRuleItineraryTravelLength
        travel_start_day: ConversionValueRule.ValueRuleItineraryTravelStartDay
    class ValueRuleItineraryAdvanceBookingWindow(proto.Message):
        min_days: int
        max_days: int
    class ValueRuleItineraryTravelLength(proto.Message):
        min_nights: int
        max_nights: int
    class ValueRuleItineraryTravelStartDay(proto.Message):
        monday: bool
        tuesday: bool
        wednesday: bool
        thursday: bool
        friday: bool
        saturday: bool
        sunday: bool
    resource_name: str
    id: int
    action: ValueRuleAction
    geo_location_condition: ValueRuleGeoLocationCondition
    device_condition: ValueRuleDeviceCondition
    audience_condition: ValueRuleAudienceCondition
    itinerary_condition: ValueRuleItineraryCondition
    owner_customer: str
    status: conversion_value_rule_status.ConversionValueRuleStatusEnum.ConversionValueRuleStatus
