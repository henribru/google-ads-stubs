from google.ads.googleads.v23.enums.types.conversion_value_rule_status import ConversionValueRuleStatusEnum
from google.ads.googleads.v23.enums.types.value_rule_geo_location_match_type import ValueRuleGeoLocationMatchTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.value_rule_geo_location_match_type import ValueRuleGeoLocationMatchTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.value_rule_device_type import ValueRuleDeviceTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v23.enums.types.value_rule_operation import ValueRuleOperationEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionValueRule(proto.Message):
    class ValueRuleAction(proto.Message):
        operation: ValueRuleOperationEnum.ValueRuleOperation
        value: float
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, operation: ValueRuleOperationEnum.ValueRuleOperation = ..., value: float = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["operation", "value"]) -> bool: ...
    class ValueRuleAudienceCondition(proto.Message):
        user_lists: MutableSequence[str]
        user_interests: MutableSequence[str]
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, user_lists: MutableSequence[str] = ..., user_interests: MutableSequence[str] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["user_lists", "user_interests"]) -> bool: ...
    class ValueRuleDeviceCondition(proto.Message):
        device_types: MutableSequence[ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, device_types: MutableSequence[ValueRuleDeviceTypeEnum.ValueRuleDeviceType] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["device_types"]) -> bool: ...
    class ValueRuleGeoLocationCondition(proto.Message):
        excluded_geo_target_constants: MutableSequence[str]
        excluded_geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
        geo_target_constants: MutableSequence[str]
        geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, excluded_geo_target_constants: MutableSequence[str] = ..., excluded_geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType = ..., geo_target_constants: MutableSequence[str] = ..., geo_match_type: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["excluded_geo_target_constants", "excluded_geo_match_type", "geo_target_constants", "geo_match_type"]) -> bool: ...
    class ValueRuleItineraryAdvanceBookingWindow(proto.Message):
        min_days: int
        max_days: int
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, min_days: int = ..., max_days: int = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["min_days", "max_days"]) -> bool: ...
    class ValueRuleItineraryCondition(proto.Message):
        advance_booking_window: ConversionValueRule.ValueRuleItineraryAdvanceBookingWindow
        travel_length: ConversionValueRule.ValueRuleItineraryTravelLength
        travel_start_day: ConversionValueRule.ValueRuleItineraryTravelStartDay
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, advance_booking_window: ConversionValueRule.ValueRuleItineraryAdvanceBookingWindow = ..., travel_length: ConversionValueRule.ValueRuleItineraryTravelLength = ..., travel_start_day: ConversionValueRule.ValueRuleItineraryTravelStartDay = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["advance_booking_window", "travel_length", "travel_start_day"]) -> bool: ...
    class ValueRuleItineraryTravelLength(proto.Message):
        min_nights: int
        max_nights: int
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, min_nights: int = ..., max_nights: int = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["min_nights", "max_nights"]) -> bool: ...
    class ValueRuleItineraryTravelStartDay(proto.Message):
        monday: bool
        tuesday: bool
        wednesday: bool
        thursday: bool
        friday: bool
        saturday: bool
        sunday: bool
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, monday: bool = ..., tuesday: bool = ..., wednesday: bool = ..., thursday: bool = ..., friday: bool = ..., saturday: bool = ..., sunday: bool = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]) -> bool: ...
    resource_name: str
    id: int
    action: ConversionValueRule.ValueRuleAction
    geo_location_condition: ConversionValueRule.ValueRuleGeoLocationCondition
    device_condition: ConversionValueRule.ValueRuleDeviceCondition
    audience_condition: ConversionValueRule.ValueRuleAudienceCondition
    itinerary_condition: ConversionValueRule.ValueRuleItineraryCondition
    owner_customer: str
    status: ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., action: ConversionValueRule.ValueRuleAction = ..., geo_location_condition: ConversionValueRule.ValueRuleGeoLocationCondition = ..., device_condition: ConversionValueRule.ValueRuleDeviceCondition = ..., audience_condition: ConversionValueRule.ValueRuleAudienceCondition = ..., itinerary_condition: ConversionValueRule.ValueRuleItineraryCondition = ..., owner_customer: str = ..., status: ConversionValueRuleStatusEnum.ConversionValueRuleStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "action", "geo_location_condition", "device_condition", "audience_condition", "itinerary_condition", "owner_customer", "status"]) -> bool: ...
