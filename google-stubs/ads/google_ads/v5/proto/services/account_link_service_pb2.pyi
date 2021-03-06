# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.resources.account_link_pb2 import (
    AccountLink as google___ads___googleads___v5___resources___account_link_pb2___AccountLink,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetAccountLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetAccountLinkRequest = GetAccountLinkRequest

class CreateAccountLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    @property
    def account_link(
        self,
    ) -> google___ads___googleads___v5___resources___account_link_pb2___AccountLink: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        account_link: typing___Optional[
            google___ads___googleads___v5___resources___account_link_pb2___AccountLink
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["account_link", b"account_link"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "account_link", b"account_link", "customer_id", b"customer_id"
        ],
    ) -> None: ...

type___CreateAccountLinkRequest = CreateAccountLinkRequest

class CreateAccountLinkResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___CreateAccountLinkResponse = CreateAccountLinkResponse

class MutateAccountLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    partial_failure: builtin___bool = ...
    validate_only: builtin___bool = ...
    @property
    def operation(self) -> type___AccountLinkOperation: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operation: typing___Optional[type___AccountLinkOperation] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["operation", b"operation"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operation",
            b"operation",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___MutateAccountLinkRequest = MutateAccountLinkRequest

class AccountLinkOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove: typing___Text = ...
    def __init__(self, *, remove: typing___Optional[typing___Text] = None,) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "operation", b"operation", "remove", b"remove"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operation", b"operation", "remove", b"remove"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["remove"]: ...

type___AccountLinkOperation = AccountLinkOperation

class MutateAccountLinkResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def result(self) -> type___MutateAccountLinkResult: ...
    def __init__(
        self, *, result: typing___Optional[type___MutateAccountLinkResult] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> None: ...

type___MutateAccountLinkResponse = MutateAccountLinkResponse

class MutateAccountLinkResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateAccountLinkResult = MutateAccountLinkResult
