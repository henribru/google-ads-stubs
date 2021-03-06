"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.enums.access_role_pb2
import google.ads.google_ads.v6.proto.enums.response_content_type_pb2
import google.ads.google_ads.v6.proto.resources.customer_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetCustomerRequest(google.protobuf.message.Message):
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

global___GetCustomerRequest = GetCustomerRequest

class MutateCustomerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    validate_only: builtins.bool = ...
    response_content_type: google.ads.google_ads.v6.proto.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.V = (
        ...
    )
    @property
    def operation(self) -> global___CustomerOperation: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        operation: typing.Optional[global___CustomerOperation] = ...,
        validate_only: builtins.bool = ...,
        response_content_type: google.ads.google_ads.v6.proto.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.V = ...,
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
            "response_content_type",
            b"response_content_type",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

global___MutateCustomerRequest = MutateCustomerRequest

class CreateCustomerClientRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    CUSTOMER_CLIENT_FIELD_NUMBER: builtins.int
    EMAIL_ADDRESS_FIELD_NUMBER: builtins.int
    ACCESS_ROLE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    email_address: typing.Text = ...
    access_role: google.ads.google_ads.v6.proto.enums.access_role_pb2.AccessRoleEnum.AccessRole.V = (
        ...
    )
    @property
    def customer_client(
        self,
    ) -> google.ads.google_ads.v6.proto.resources.customer_pb2.Customer: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        customer_client: typing.Optional[
            google.ads.google_ads.v6.proto.resources.customer_pb2.Customer
        ] = ...,
        email_address: typing.Text = ...,
        access_role: google.ads.google_ads.v6.proto.enums.access_role_pb2.AccessRoleEnum.AccessRole.V = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_email_address",
            b"_email_address",
            "customer_client",
            b"customer_client",
            "email_address",
            b"email_address",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
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
        oneof_group: typing_extensions.Literal["_email_address", b"_email_address"],
    ) -> typing_extensions.Literal["email_address"]: ...

global___CreateCustomerClientRequest = CreateCustomerClientRequest

class CustomerOperation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def update(
        self,
    ) -> google.ads.google_ads.v6.proto.resources.customer_pb2.Customer: ...
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    def __init__(
        self,
        *,
        update: typing.Optional[
            google.ads.google_ads.v6.proto.resources.customer_pb2.Customer
        ] = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "update", b"update", "update_mask", b"update_mask"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "update", b"update", "update_mask", b"update_mask"
        ],
    ) -> None: ...

global___CustomerOperation = CustomerOperation

class CreateCustomerClientResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    INVITATION_LINK_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    invitation_link: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        invitation_link: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "invitation_link", b"invitation_link", "resource_name", b"resource_name"
        ],
    ) -> None: ...

global___CreateCustomerClientResponse = CreateCustomerClientResponse

class MutateCustomerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___MutateCustomerResult: ...
    def __init__(
        self,
        *,
        result: typing.Optional[global___MutateCustomerResult] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["result", b"result"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["result", b"result"]
    ) -> None: ...

global___MutateCustomerResponse = MutateCustomerResponse

class MutateCustomerResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CUSTOMER_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    @property
    def customer(
        self,
    ) -> google.ads.google_ads.v6.proto.resources.customer_pb2.Customer: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        customer: typing.Optional[
            google.ads.google_ads.v6.proto.resources.customer_pb2.Customer
        ] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["customer", b"customer"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "customer", b"customer", "resource_name", b"resource_name"
        ],
    ) -> None: ...

global___MutateCustomerResult = MutateCustomerResult

class ListAccessibleCustomersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(
        self,
    ) -> None: ...

global___ListAccessibleCustomersRequest = ListAccessibleCustomersRequest

class ListAccessibleCustomersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    resource_names: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        typing.Text
    ] = ...
    def __init__(
        self,
        *,
        resource_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_names", b"resource_names"]
    ) -> None: ...

global___ListAccessibleCustomersResponse = ListAccessibleCustomersResponse
