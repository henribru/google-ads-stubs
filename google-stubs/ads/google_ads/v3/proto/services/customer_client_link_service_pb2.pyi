# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v3.proto.resources.customer_client_link_pb2 import (
    CustomerClientLink as google___ads___googleads___v3___resources___customer_client_link_pb2___CustomerClientLink,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetCustomerClientLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetCustomerClientLinkRequest = GetCustomerClientLinkRequest

class MutateCustomerClientLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    @property
    def operation(self) -> type___CustomerClientLinkOperation: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operation: typing___Optional[type___CustomerClientLinkOperation] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["operation", b"operation"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id", b"customer_id", "operation", b"operation"
        ],
    ) -> None: ...

type___MutateCustomerClientLinkRequest = MutateCustomerClientLinkRequest

class CustomerClientLinkOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v3___resources___customer_client_link_pb2___CustomerClientLink: ...
    @property
    def update(
        self,
    ) -> google___ads___googleads___v3___resources___customer_client_link_pb2___CustomerClientLink: ...
    def __init__(
        self,
        *,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
        create: typing___Optional[
            google___ads___googleads___v3___resources___customer_client_link_pb2___CustomerClientLink
        ] = None,
        update: typing___Optional[
            google___ads___googleads___v3___resources___customer_client_link_pb2___CustomerClientLink
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create", "update"]: ...

type___CustomerClientLinkOperation = CustomerClientLinkOperation

class MutateCustomerClientLinkResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def result(self) -> type___MutateCustomerClientLinkResult: ...
    def __init__(
        self,
        *,
        result: typing___Optional[type___MutateCustomerClientLinkResult] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> None: ...

type___MutateCustomerClientLinkResponse = MutateCustomerClientLinkResponse

class MutateCustomerClientLinkResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateCustomerClientLinkResult = MutateCustomerClientLinkResult
