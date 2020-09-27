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
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.enums.geo_target_constant_status_pb2 import (
    GeoTargetConstantStatusEnum as google___ads___googleads___v4___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GeoTargetConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v4___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum.GeoTargetConstantStatusValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def target_type(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def canonical_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        target_type: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v4___enums___geo_target_constant_status_pb2___GeoTargetConstantStatusEnum.GeoTargetConstantStatusValue
        ] = None,
        canonical_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "canonical_name",
            b"canonical_name",
            "country_code",
            b"country_code",
            "id",
            b"id",
            "name",
            b"name",
            "target_type",
            b"target_type",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "canonical_name",
            b"canonical_name",
            "country_code",
            b"country_code",
            "id",
            b"id",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "target_type",
            b"target_type",
        ],
    ) -> None: ...

type___GeoTargetConstant = GeoTargetConstant
