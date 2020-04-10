# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.enums.placement_type_pb2 import (
    PlacementTypeEnum as google___ads___googleads___v3___enums___placement_type_pb2___PlacementTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class DetailPlacementView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    placement_type = (
        ...
    )  # type: google___ads___googleads___v3___enums___placement_type_pb2___PlacementTypeEnum.PlacementType
    @property
    def placement(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def display_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def group_placement_target_url(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def target_url(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        placement: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        display_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        group_placement_target_url: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        target_url: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        placement_type: typing___Optional[
            google___ads___googleads___v3___enums___placement_type_pb2___PlacementTypeEnum.PlacementType
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DetailPlacementView: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> DetailPlacementView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "display_name",
            b"display_name",
            "group_placement_target_url",
            b"group_placement_target_url",
            "placement",
            b"placement",
            "target_url",
            b"target_url",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "display_name",
            b"display_name",
            "group_placement_target_url",
            b"group_placement_target_url",
            "placement",
            b"placement",
            "placement_type",
            b"placement_type",
            "resource_name",
            b"resource_name",
            "target_url",
            b"target_url",
        ],
    ) -> None: ...

global___DetailPlacementView = DetailPlacementView
