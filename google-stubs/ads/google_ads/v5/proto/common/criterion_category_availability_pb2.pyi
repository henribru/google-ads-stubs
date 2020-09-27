# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Iterable as typing___Iterable, Optional as typing___Optional

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.advertising_channel_sub_type_pb2 import (
    AdvertisingChannelSubTypeEnum as google___ads___googleads___v5___enums___advertising_channel_sub_type_pb2___AdvertisingChannelSubTypeEnum,
)
from google.ads.google_ads.v5.proto.enums.advertising_channel_type_pb2 import (
    AdvertisingChannelTypeEnum as google___ads___googleads___v5___enums___advertising_channel_type_pb2___AdvertisingChannelTypeEnum,
)
from google.ads.google_ads.v5.proto.enums.criterion_category_channel_availability_mode_pb2 import (
    CriterionCategoryChannelAvailabilityModeEnum as google___ads___googleads___v5___enums___criterion_category_channel_availability_mode_pb2___CriterionCategoryChannelAvailabilityModeEnum,
)
from google.ads.google_ads.v5.proto.enums.criterion_category_locale_availability_mode_pb2 import (
    CriterionCategoryLocaleAvailabilityModeEnum as google___ads___googleads___v5___enums___criterion_category_locale_availability_mode_pb2___CriterionCategoryLocaleAvailabilityModeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CriterionCategoryAvailability(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def channel(self) -> type___CriterionCategoryChannelAvailability: ...
    @property
    def locale(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___CriterionCategoryLocaleAvailability
    ]: ...
    def __init__(
        self,
        *,
        channel: typing___Optional[type___CriterionCategoryChannelAvailability] = None,
        locale: typing___Optional[
            typing___Iterable[type___CriterionCategoryLocaleAvailability]
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["channel", b"channel"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "channel", b"channel", "locale", b"locale"
        ],
    ) -> None: ...

type___CriterionCategoryAvailability = CriterionCategoryAvailability

class CriterionCategoryChannelAvailability(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    availability_mode: google___ads___googleads___v5___enums___criterion_category_channel_availability_mode_pb2___CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityModeValue = ...
    advertising_channel_type: google___ads___googleads___v5___enums___advertising_channel_type_pb2___AdvertisingChannelTypeEnum.AdvertisingChannelTypeValue = ...
    advertising_channel_sub_type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        google___ads___googleads___v5___enums___advertising_channel_sub_type_pb2___AdvertisingChannelSubTypeEnum.AdvertisingChannelSubTypeValue
    ] = ...
    @property
    def include_default_channel_sub_type(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        availability_mode: typing___Optional[
            google___ads___googleads___v5___enums___criterion_category_channel_availability_mode_pb2___CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityModeValue
        ] = None,
        advertising_channel_type: typing___Optional[
            google___ads___googleads___v5___enums___advertising_channel_type_pb2___AdvertisingChannelTypeEnum.AdvertisingChannelTypeValue
        ] = None,
        advertising_channel_sub_type: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v5___enums___advertising_channel_sub_type_pb2___AdvertisingChannelSubTypeEnum.AdvertisingChannelSubTypeValue
            ]
        ] = None,
        include_default_channel_sub_type: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "include_default_channel_sub_type", b"include_default_channel_sub_type"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "advertising_channel_sub_type",
            b"advertising_channel_sub_type",
            "advertising_channel_type",
            b"advertising_channel_type",
            "availability_mode",
            b"availability_mode",
            "include_default_channel_sub_type",
            b"include_default_channel_sub_type",
        ],
    ) -> None: ...

type___CriterionCategoryChannelAvailability = CriterionCategoryChannelAvailability

class CriterionCategoryLocaleAvailability(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    availability_mode: google___ads___googleads___v5___enums___criterion_category_locale_availability_mode_pb2___CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue = ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        availability_mode: typing___Optional[
            google___ads___googleads___v5___enums___criterion_category_locale_availability_mode_pb2___CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue
        ] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "country_code", b"country_code", "language_code", b"language_code"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "availability_mode",
            b"availability_mode",
            "country_code",
            b"country_code",
            "language_code",
            b"language_code",
        ],
    ) -> None: ...

type___CriterionCategoryLocaleAvailability = CriterionCategoryLocaleAvailability
