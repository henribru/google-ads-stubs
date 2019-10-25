# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.resources.customer_manager_link_pb2 import (
    CustomerManagerLink as google___ads___googleads___v1___resources___customer_manager_link_pb2___CustomerManagerLink,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetCustomerManagerLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomerManagerLinkRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class MutateCustomerManagerLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text

    @property
    def operations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CustomerManagerLinkOperation]: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operations : typing___Optional[typing___Iterable[CustomerManagerLinkOperation]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateCustomerManagerLinkRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operations"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operations",b"operations"]) -> None: ...

class CustomerManagerLinkOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...

    @property
    def update(self) -> google___ads___googleads___v1___resources___customer_manager_link_pb2___CustomerManagerLink: ...

    def __init__(self,
        *,
        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
        update : typing___Optional[google___ads___googleads___v1___resources___customer_manager_link_pb2___CustomerManagerLink] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CustomerManagerLinkOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"operation",u"update",u"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"operation",u"update",u"update_mask"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"operation",b"operation",u"update",b"update",u"update_mask",b"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"operation",b"operation",u"update",b"update",u"update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["update"]: ...

class MutateCustomerManagerLinkResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[MutateCustomerManagerLinkResult]: ...

    def __init__(self,
        *,
        results : typing___Optional[typing___Iterable[MutateCustomerManagerLinkResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateCustomerManagerLinkResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"results"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"results",b"results"]) -> None: ...

class MutateCustomerManagerLinkResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateCustomerManagerLinkResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
