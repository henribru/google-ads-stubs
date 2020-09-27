# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)
from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.access_role_pb2 import (
    AccessRoleEnum as google___ads___googleads___v5___enums___access_role_pb2___AccessRoleEnum,
)
from google.ads.google_ads.v5.proto.enums.response_content_type_pb2 import (
    ResponseContentTypeEnum as google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum,
)
from google.ads.google_ads.v5.proto.resources.customer_pb2 import (
    Customer as google___ads___googleads___v5___resources___customer_pb2___Customer,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetCustomerRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetCustomerRequest = GetCustomerRequest

class MutateCustomerRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    validate_only: builtin___bool = ...
    response_content_type: google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum.ResponseContentTypeValue = ...
    @property
    def operation(self) -> type___CustomerOperation: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operation: typing___Optional[type___CustomerOperation] = None,
        validate_only: typing___Optional[builtin___bool] = None,
        response_content_type: typing___Optional[
            google___ads___googleads___v5___enums___response_content_type_pb2___ResponseContentTypeEnum.ResponseContentTypeValue
        ] = None,
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
            "response_content_type",
            b"response_content_type",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___MutateCustomerRequest = MutateCustomerRequest

class CreateCustomerClientRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    email_address: typing___Text = ...
    access_role: google___ads___googleads___v5___enums___access_role_pb2___AccessRoleEnum.AccessRoleValue = ...
    @property
    def customer_client(
        self,
    ) -> google___ads___googleads___v5___resources___customer_pb2___Customer: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        customer_client: typing___Optional[
            google___ads___googleads___v5___resources___customer_pb2___Customer
        ] = None,
        email_address: typing___Optional[typing___Text] = None,
        access_role: typing___Optional[
            google___ads___googleads___v5___enums___access_role_pb2___AccessRoleEnum.AccessRoleValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_email_address",
            b"_email_address",
            "customer_client",
            b"customer_client",
            "email_address",
            b"email_address",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_email_address",
            b"_email_address",
            "access_role",
            b"access_role",
            "customer_client",
            b"customer_client",
            "customer_id",
            b"customer_id",
            "email_address",
            b"email_address",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_email_address", b"_email_address"],
    ) -> typing_extensions___Literal["email_address"]: ...

type___CreateCustomerClientRequest = CreateCustomerClientRequest

class CustomerOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def update(
        self,
    ) -> google___ads___googleads___v5___resources___customer_pb2___Customer: ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    def __init__(
        self,
        *,
        update: typing___Optional[
            google___ads___googleads___v5___resources___customer_pb2___Customer
        ] = None,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "update", b"update", "update_mask", b"update_mask"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "update", b"update", "update_mask", b"update_mask"
        ],
    ) -> None: ...

type___CustomerOperation = CustomerOperation

class CreateCustomerClientResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    invitation_link: typing___Text = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        invitation_link: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "invitation_link", b"invitation_link", "resource_name", b"resource_name"
        ],
    ) -> None: ...

type___CreateCustomerClientResponse = CreateCustomerClientResponse

class MutateCustomerResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def result(self) -> type___MutateCustomerResult: ...
    def __init__(
        self, *, result: typing___Optional[type___MutateCustomerResult] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> None: ...

type___MutateCustomerResponse = MutateCustomerResponse

class MutateCustomerResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    @property
    def customer(
        self,
    ) -> google___ads___googleads___v5___resources___customer_pb2___Customer: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        customer: typing___Optional[
            google___ads___googleads___v5___resources___customer_pb2___Customer
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["customer", b"customer"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer", b"customer", "resource_name", b"resource_name"
        ],
    ) -> None: ...

type___MutateCustomerResult = MutateCustomerResult

class ListAccessibleCustomersRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...

type___ListAccessibleCustomersRequest = ListAccessibleCustomersRequest

class ListAccessibleCustomersResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_names: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    def __init__(
        self,
        *,
        resource_names: typing___Optional[typing___Iterable[typing___Text]] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["resource_names", b"resource_names"],
    ) -> None: ...

type___ListAccessibleCustomersResponse = ListAccessibleCustomersResponse
