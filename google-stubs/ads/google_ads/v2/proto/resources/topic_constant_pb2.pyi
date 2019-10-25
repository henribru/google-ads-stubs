# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class TopicConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def topic_constant_parent(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def path(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        topic_constant_parent : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        path : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TopicConstant: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"id",u"topic_constant_parent"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",u"path",u"resource_name",u"topic_constant_parent"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"topic_constant_parent",b"topic_constant_parent"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"path",b"path",u"resource_name",b"resource_name",u"topic_constant_parent",b"topic_constant_parent"]) -> None: ...
