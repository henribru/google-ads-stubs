# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class AdGroupCriterionLabel(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    @property
    def ad_group_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def label(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ad_group_criterion : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        label : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdGroupCriterionLabel: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group_criterion",u"label"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group_criterion",u"label",u"resource_name"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group_criterion",b"ad_group_criterion",u"label",b"label"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group_criterion",b"ad_group_criterion",u"label",b"label",u"resource_name",b"resource_name"]) -> None: ...
