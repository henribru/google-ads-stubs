# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.resources.ad_group_bid_modifier_pb2 import (
    AdGroupBidModifier as google___ads___googleads___v2___resources___ad_group_bid_modifier_pb2___AdGroupBidModifier,
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

from google.rpc.status_pb2 import (
    Status as google___rpc___status_pb2___Status,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetAdGroupBidModifierRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetAdGroupBidModifierRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class MutateAdGroupBidModifiersRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text
    partial_failure = ... # type: bool
    validate_only = ... # type: bool

    @property
    def operations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AdGroupBidModifierOperation]: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operations : typing___Optional[typing___Iterable[AdGroupBidModifierOperation]] = None,
        partial_failure : typing___Optional[bool] = None,
        validate_only : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateAdGroupBidModifiersRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operations",u"partial_failure",u"validate_only"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operations",b"operations",u"partial_failure",b"partial_failure",u"validate_only",b"validate_only"]) -> None: ...

class AdGroupBidModifierOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove = ... # type: typing___Text

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...

    @property
    def create(self) -> google___ads___googleads___v2___resources___ad_group_bid_modifier_pb2___AdGroupBidModifier: ...

    @property
    def update(self) -> google___ads___googleads___v2___resources___ad_group_bid_modifier_pb2___AdGroupBidModifier: ...

    def __init__(self,
        *,
        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
        create : typing___Optional[google___ads___googleads___v2___resources___ad_group_bid_modifier_pb2___AdGroupBidModifier] = None,
        update : typing___Optional[google___ads___googleads___v2___resources___ad_group_bid_modifier_pb2___AdGroupBidModifier] = None,
        remove : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdGroupBidModifierOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove",u"update",u"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove",u"update",u"update_mask"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["create","update","remove"]: ...

class MutateAdGroupBidModifiersResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[MutateAdGroupBidModifierResult]: ...

    def __init__(self,
        *,
        partial_failure_error : typing___Optional[google___rpc___status_pb2___Status] = None,
        results : typing___Optional[typing___Iterable[MutateAdGroupBidModifierResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateAdGroupBidModifiersResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",u"results"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error",u"results",b"results"]) -> None: ...

class MutateAdGroupBidModifierResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateAdGroupBidModifierResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
