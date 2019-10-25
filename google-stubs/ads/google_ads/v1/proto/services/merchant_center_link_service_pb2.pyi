# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.resources.merchant_center_link_pb2 import (
    MerchantCenterLink as google___ads___googleads___v1___resources___merchant_center_link_pb2___MerchantCenterLink,
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


class ListMerchantCenterLinksRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListMerchantCenterLinksRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id"]) -> None: ...

class ListMerchantCenterLinksResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def merchant_center_links(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___resources___merchant_center_link_pb2___MerchantCenterLink]: ...

    def __init__(self,
        *,
        merchant_center_links : typing___Optional[typing___Iterable[google___ads___googleads___v1___resources___merchant_center_link_pb2___MerchantCenterLink]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListMerchantCenterLinksResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"merchant_center_links"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"merchant_center_links",b"merchant_center_links"]) -> None: ...

class GetMerchantCenterLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetMerchantCenterLinkRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class MutateMerchantCenterLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text

    @property
    def operation(self) -> MerchantCenterLinkOperation: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operation : typing___Optional[MerchantCenterLinkOperation] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateMerchantCenterLinkRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"operation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operation"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"operation",b"operation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operation",b"operation"]) -> None: ...

class MerchantCenterLinkOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove = ... # type: typing___Text

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...

    @property
    def update(self) -> google___ads___googleads___v1___resources___merchant_center_link_pb2___MerchantCenterLink: ...

    def __init__(self,
        *,
        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
        update : typing___Optional[google___ads___googleads___v1___resources___merchant_center_link_pb2___MerchantCenterLink] = None,
        remove : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MerchantCenterLinkOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"operation",u"remove",u"update",u"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"operation",u"remove",u"update",u"update_mask"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["update","remove"]: ...

class MutateMerchantCenterLinkResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def result(self) -> MutateMerchantCenterLinkResult: ...

    def __init__(self,
        *,
        result : typing___Optional[MutateMerchantCenterLinkResult] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateMerchantCenterLinkResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"result"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> None: ...

class MutateMerchantCenterLinkResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateMerchantCenterLinkResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
