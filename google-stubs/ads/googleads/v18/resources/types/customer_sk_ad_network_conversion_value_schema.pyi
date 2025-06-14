import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import sk_ad_network_coarse_conversion_value
from typing import MutableSequence

__protobuf__: Incomplete

class CustomerSkAdNetworkConversionValueSchema(proto.Message):
    class SkAdNetworkConversionValueSchema(proto.Message):
        class FineGrainedConversionValueMappings(proto.Message):
            fine_grained_conversion_value: int
            conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
        class PostbackMapping(proto.Message):
            postback_sequence_index: int
            coarse_grained_conversion_value_mappings: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.CoarseGrainedConversionValueMappings
            lock_window_coarse_conversion_value: sk_ad_network_coarse_conversion_value.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
            lock_window_fine_conversion_value: int
            lock_window_event: str
        class CoarseGrainedConversionValueMappings(proto.Message):
            low_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            medium_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            high_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
        class ConversionValueMapping(proto.Message):
            min_time_post_install_hours: int
            max_time_post_install_hours: int
            mapped_events: MutableSequence['CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event']
        class Event(proto.Message):
            class RevenueRange(proto.Message):
                min_event_revenue: float
                max_event_revenue: float
            class EventOccurrenceRange(proto.Message):
                min_event_count: int
                max_event_count: int
            mapped_event_name: str
            currency_code: str
            event_revenue_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.RevenueRange
            event_revenue_value: float
            event_occurrence_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.EventOccurrenceRange
            event_counter: int
        app_id: str
        measurement_window_hours: int
        fine_grained_conversion_value_mappings: MutableSequence['CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.FineGrainedConversionValueMappings']
        postback_mappings: MutableSequence['CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.PostbackMapping']
    resource_name: str
    schema: SkAdNetworkConversionValueSchema
