# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.operating_system_version_operator_type_pb2 import (
    OperatingSystemVersionOperatorTypeEnum as google___ads___googleads___v5___enums___operating_system_version_operator_type_pb2___OperatingSystemVersionOperatorTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class OperatingSystemVersionConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    name: typing___Text = ...
    os_major_version: builtin___int = ...
    os_minor_version: builtin___int = ...
    operator_type: google___ads___googleads___v5___enums___operating_system_version_operator_type_pb2___OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorTypeValue = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        name: typing___Optional[typing___Text] = None,
        os_major_version: typing___Optional[builtin___int] = None,
        os_minor_version: typing___Optional[builtin___int] = None,
        operator_type: typing___Optional[
            google___ads___googleads___v5___enums___operating_system_version_operator_type_pb2___OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorTypeValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_os_major_version",
            b"_os_major_version",
            "_os_minor_version",
            b"_os_minor_version",
            "id",
            b"id",
            "name",
            b"name",
            "os_major_version",
            b"os_major_version",
            "os_minor_version",
            b"os_minor_version",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_os_major_version",
            b"_os_major_version",
            "_os_minor_version",
            b"_os_minor_version",
            "id",
            b"id",
            "name",
            b"name",
            "operator_type",
            b"operator_type",
            "os_major_version",
            b"os_major_version",
            "os_minor_version",
            b"os_minor_version",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_os_major_version", b"_os_major_version"
        ],
    ) -> typing_extensions___Literal["os_major_version"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_os_minor_version", b"_os_minor_version"
        ],
    ) -> typing_extensions___Literal["os_minor_version"]: ...

type___OperatingSystemVersionConstant = OperatingSystemVersionConstant
