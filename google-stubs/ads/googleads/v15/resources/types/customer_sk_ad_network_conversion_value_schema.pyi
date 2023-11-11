from collections.abc import MutableSequence
from typing import Any

import proto

class CustomerSkAdNetworkConversionValueSchema(proto.Message):
    class SkAdNetworkConversionValueSchema(proto.Message):
        class ConversionValueMapping(proto.Message):
            min_time_post_install_hours: int
            max_time_post_install_hours: int
            mapped_events: MutableSequence[
                CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event
            ]
            def __init__(
                self,
                mapping: Any | None = ...,
                *,
                ignore_unknown_fields: bool = ...,
                min_time_post_install_hours: int = ...,
                max_time_post_install_hours: int = ...,
                mapped_events: MutableSequence[
                    CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event
                ] = ...
            ) -> None: ...

        class Event(proto.Message):
            class EventOccurrenceRange(proto.Message):
                min_event_count: int
                max_event_count: int
                def __init__(
                    self,
                    mapping: Any | None = ...,
                    *,
                    ignore_unknown_fields: bool = ...,
                    min_event_count: int = ...,
                    max_event_count: int = ...
                ) -> None: ...

            class RevenueRange(proto.Message):
                min_event_revenue: float
                max_event_revenue: float
                def __init__(
                    self,
                    mapping: Any | None = ...,
                    *,
                    ignore_unknown_fields: bool = ...,
                    min_event_revenue: float = ...,
                    max_event_revenue: float = ...
                ) -> None: ...
            mapped_event_name: str
            currency_code: str
            event_revenue_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.RevenueRange
            event_revenue_value: float
            event_occurrence_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.EventOccurrenceRange
            event_counter: int
            def __init__(
                self,
                mapping: Any | None = ...,
                *,
                ignore_unknown_fields: bool = ...,
                mapped_event_name: str = ...,
                currency_code: str = ...,
                event_revenue_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.RevenueRange = ...,
                event_revenue_value: float = ...,
                event_occurrence_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.EventOccurrenceRange = ...,
                event_counter: int = ...
            ) -> None: ...

        class FineGrainedConversionValueMappings(proto.Message):
            fine_grained_conversion_value: int
            conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            def __init__(
                self,
                mapping: Any | None = ...,
                *,
                ignore_unknown_fields: bool = ...,
                fine_grained_conversion_value: int = ...,
                conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping = ...
            ) -> None: ...
        app_id: str
        measurement_window_hours: int
        fine_grained_conversion_value_mappings: MutableSequence[
            CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.FineGrainedConversionValueMappings
        ]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            app_id: str = ...,
            measurement_window_hours: int = ...,
            fine_grained_conversion_value_mappings: MutableSequence[
                CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.FineGrainedConversionValueMappings
            ] = ...
        ) -> None: ...
    resource_name: str
    schema: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        schema: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema = ...
    ) -> None: ...
