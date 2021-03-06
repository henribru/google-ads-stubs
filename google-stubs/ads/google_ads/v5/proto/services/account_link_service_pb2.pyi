"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.resources.account_link_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetAccountLinkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___GetAccountLinkRequest = GetAccountLinkRequest

class CreateAccountLinkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    ACCOUNT_LINK_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    @property
    def account_link(
        self,
    ) -> google.ads.google_ads.v5.proto.resources.account_link_pb2.AccountLink: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        account_link: typing.Optional[
            google.ads.google_ads.v5.proto.resources.account_link_pb2.AccountLink
        ] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["account_link", b"account_link"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "account_link", b"account_link", "customer_id", b"customer_id"
        ],
    ) -> None: ...

global___CreateAccountLinkRequest = CreateAccountLinkRequest

class CreateAccountLinkResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___CreateAccountLinkResponse = CreateAccountLinkResponse

class MutateAccountLinkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    partial_failure: builtins.bool = ...
    validate_only: builtins.bool = ...
    @property
    def operation(self) -> global___AccountLinkOperation: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        operation: typing.Optional[global___AccountLinkOperation] = ...,
        partial_failure: builtins.bool = ...,
        validate_only: builtins.bool = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["operation", b"operation"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
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

global___MutateAccountLinkRequest = MutateAccountLinkRequest

class AccountLinkOperation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REMOVE_FIELD_NUMBER: builtins.int
    remove: typing.Text = ...
    def __init__(
        self,
        *,
        remove: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "operation", b"operation", "remove", b"remove"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "operation", b"operation", "remove", b"remove"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["operation", b"operation"]
    ) -> typing_extensions.Literal["remove"]: ...

global___AccountLinkOperation = AccountLinkOperation

class MutateAccountLinkResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___MutateAccountLinkResult: ...
    def __init__(
        self,
        *,
        result: typing.Optional[global___MutateAccountLinkResult] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["result", b"result"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["result", b"result"]
    ) -> None: ...

global___MutateAccountLinkResponse = MutateAccountLinkResponse

class MutateAccountLinkResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___MutateAccountLinkResult = MutateAccountLinkResult
