# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.enums.geo_targeting_type_pb2 import (
    GeoTargetingTypeEnum as google___ads___googleads___v4___enums___geo_targeting_type_pb2___GeoTargetingTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GeographicView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    location_type: google___ads___googleads___v4___enums___geo_targeting_type_pb2___GeoTargetingTypeEnum.GeoTargetingTypeValue = ...
    @property
    def country_criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        location_type: typing___Optional[
            google___ads___googleads___v4___enums___geo_targeting_type_pb2___GeoTargetingTypeEnum.GeoTargetingTypeValue
        ] = None,
        country_criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "country_criterion_id", b"country_criterion_id"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "country_criterion_id",
            b"country_criterion_id",
            "location_type",
            b"location_type",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

type___GeographicView = GeographicView
