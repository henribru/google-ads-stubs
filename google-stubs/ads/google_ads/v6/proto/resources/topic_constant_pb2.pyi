# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TopicConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    topic_constant_parent: typing___Text = ...
    path: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        topic_constant_parent: typing___Optional[typing___Text] = None,
        path: typing___Optional[typing___Iterable[typing___Text]] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_id",
            b"_id",
            "_topic_constant_parent",
            b"_topic_constant_parent",
            "id",
            b"id",
            "topic_constant_parent",
            b"topic_constant_parent",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_id",
            b"_id",
            "_topic_constant_parent",
            b"_topic_constant_parent",
            "id",
            b"id",
            "path",
            b"path",
            "resource_name",
            b"resource_name",
            "topic_constant_parent",
            b"topic_constant_parent",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_topic_constant_parent", b"_topic_constant_parent"
        ],
    ) -> typing_extensions___Literal["topic_constant_parent"]: ...

type___TopicConstant = TopicConstant